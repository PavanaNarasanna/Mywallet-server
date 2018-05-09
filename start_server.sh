#!/usr/bin/env bash

# Attempting to setup the Flask server as a "large" application.
# See http://flask.pocoo.org/docs/0.12/patterns/packages/
# See this issue for more information
# https://github.com/pallets/flask/issues/1847

if [[ $PATH != *":/venv/bin:"* ]]
then
  echo "Activating Virtual Environment"
  virtualenv venv
  . venv/bin/activate
  pip install -r requirements.txt
fi

export FLASK_APP=server
export DATABASE_URL="postgresql://$(whoami)@localhost/lp02_team_s_server"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Starting server <${FLASK_APP}> ..."
python -m flask run --with-threads
