#!/usr/bin/env python

import os
from datetime import timedelta, datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity
from flask_graphql import GraphQLView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from server.database.database import Base, db_session
from .config import Config
from server.schema import schema
from server.config import Config
from server.database import user_ops


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['JWT_AUTH_USERNAME_KEY'] = 'email_id'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(7 * 24 * 60 * 60)
app.config['JWT_AUTH_URL_RULE'] = '/auth'
app.config['JWT_USER_IDENTITY_FIELD'] = 'email_id'

MIGRATION_DIR = os.path.join('server', 'migrations')

migrate = Migrate(app, Base, directory=MIGRATION_DIR)

CORS(app)

user = user_ops.Users()
jwt = JWT(app, user.authenticate, user.identity)


@jwt.jwt_payload_handler
def jwt_payload_handler(user):
    iat = datetime.utcnow()
    exp = iat + app.config.get('JWT_EXPIRATION_DELTA')
    nbf = iat + app.config.get('JWT_NOT_BEFORE_DELTA')
    user_identity_field = app.config.get('JWT_USER_IDENTITY_FIELD', 'id')
    email_id = getattr(user, user_identity_field) or user[user_identity_field]
    return {'exp': exp, 'iat': iat, 'nbf': nbf, 'identity': email_id}


# This is a sample route.
@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity.last_name


@app.route('/getme')
@jwt_required()
def getme():
    return jsonify(
        firstName=current_identity.first_name,
        lastName=current_identity.last_name,
        email_id=current_identity.email_id,
    )


@app.route('/')
def welcome():
    return """Welcome to MyWallet Server project"""

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
    