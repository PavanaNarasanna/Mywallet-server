#!/usr/bin/env python

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_graphql import GraphQLView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from server.database.database import Base, db_session
from .config import Config
from server.schema import schema
from server.config import Config
from .amazonS3 import get_file_from_s3
# from server.ml_analyser_engine import process_chart

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['DEBUG'] = os.environ.get('DEBUG', 'True').upper() == 'TRUE'

MIGRATION_DIR = os.path.join('server', 'migrations')

migrate = Migrate(app, Base, directory=MIGRATION_DIR)

CORS(app)

@app.route('/')
def welcome():
    return """Welcome to the LauchPad 2 Team S project"""

# Useful for having the GraphiQL interface.
app.add_url_rule('/graphql', view_func=(GraphQLView.as_view('graphql',
                                                            schema=schema,
                                                            graphiql=True,
                                                            context={'session': db_session,'app_mode':'execution'})))

# Dev graphQL endpoints which will NOT require JWT tokens.
if app.config.get('DEBUG', False):
    app.add_url_rule('/graphql-debug', view_func=GraphQLView.as_view('graphql-debug',
                                                                     schema=schema,
                                                                     graphiql=True,
                                                                     context={'session': db_session,'app_mode':'debug'}))


@app.route('/static/pdfs/<filename>')
def serve_pdf(filename):
    file = get_file_from_s3(filename)
    return file['Body'].read()


@app.route('/process/pdf', methods=['POST'])
def process_pdf():
    if 'chart' in request.files:
        process_chart(request.files['chart'], cp=('cp' in request.form))
        return 'Success'
    else:
        return 'There was an issue'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
