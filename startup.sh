#!/usr/bin/env sh

# wait until mysql server is ready
/wait

chmod +x /code/collect_data

# start Flask web app
python3 app.py
