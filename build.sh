#!/usr/bin/env bash

make migrate

python3 manage.py collectstatic
