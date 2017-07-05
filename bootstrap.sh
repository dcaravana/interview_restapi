#!/bin/bash

PROJECT=interview_tangent
ENV_BASE=~/envs
ENV=$ENV_BASE/$PROJECT-python

if [[ ! -d $ENV ]]; then
    mkdir -p $ENV
    virtualenv --no-site-packages $ENV
fi

$ENV/bin/pip install -r requirements.txt

python setup.py develop
