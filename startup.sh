#!/usr/bin/env sh

# wait until mysql server is ready
/wait

# start Flask web app
python3 app.py
