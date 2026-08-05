#!/bin/bash
echo "BUILD START"
python3 -m pip install --break-system-packages -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "BUILD END"
