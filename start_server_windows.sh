#!/usr/bin/env bash

if [ ! -d "venv/Scripts" ]; then
  echo "Installing Virtual Environment"
  virtualenv venv
fi

. venv/Scripts/activate
pip install -r requirements.txt

export FLASK_APP=server
export DATABASE_URL="postgresql://postgres:password-1@localhost/wallet"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Starting server <${FLASK_APP}> ..."
python -m flask run --with-threads
