#!/usr/bin/env bash

if [[ $PATH != *":/venv/bin:"* ]]
then
  echo "Activating Virtual Environment"
  virtualenv venv
  . venv/bin/activate
  pip install -r requirements.txt
  pip install -e .
fi

export FLASK_APP=server
export DATABASE_URL="postgresql://$(whoami)@localhost/lp02_team_s_server"

py.test --cov server --verbose