#!/bin/bash

PROJECT=interview_restapi
ENV_BASE=~/.virtualenvs
ENV=$ENV_BASE/$PROJECT-python

if [[ ! -d $ENV ]]; then
    mkdir -p $ENV
    # add -p python3 
    virtualenv --no-site-packages $ENV
    $ENV/bin/pip install --upgrade pip #else cryptography install fails
fi

$ENV/bin/pip install -r requirements.txt

source $ENV/bin/activate

python setup.py develop

echo
echo Now do:
echo source $ENV/bin/activate
echo ./manage.py migrate
echo ./manage.py createsuperuser --username admin --email admin@nowhere.no
echo [enter \"admin001\" as password]
echo ./manage.py runserver
