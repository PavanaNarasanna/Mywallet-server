#!/usr/bin/env bash

if [ ! -d "venv/Scripts" ]; then 
  echo "Installing Virtual Environment"
  virtualenv venv
fi

. venv/Scripts/activate
pip install -r requirements.txt
pip install --upgrade autopep8
pip install -e .

export FLASK_APP=server
export DATABASE_URL="postgresql://$(whoami)@localhost/lp02_team_s_servertest"

py.test --cov server --verbose
