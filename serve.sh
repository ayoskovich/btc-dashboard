#!/bin/bash
export FLASK_APP=flask_btc.py
export FLASK_DEBUG=1
export FLASK_ENV=development

flask run -h 192.168.1.215
