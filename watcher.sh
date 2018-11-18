#!/bin/bash
. venv/bin/activate
nodemon --ext py --exec "clear;ctags -R;nosetests;"
