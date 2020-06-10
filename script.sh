#!/bin/bash

# Random prayer request script for cron
# @sonbyj01

# add script to crontab to run every Wednesday at 10:00 am:
# $ crontab -e
# 0 10 * * 3 /home/helen/projects/prayer_request/script.sh

# sources the virtual environment needed to run the program
source /home/helen/projects/prayer_request/venv/bin/activate

# moves into project directory
cd /home/helen/projects/prayer_request

# turns to executable
chmod +x /home/helen/projects/prayer_request/rand_and_send.py

# runs the program
/home/helen/projects/prayer_request/rand_and_send.py

# deactivates the virtual environment
deactivate
