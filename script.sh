#!/bin/bash

# Random prayer request script for cron
# @sonbyj01

# add script to crontab to run every Wednesday at 10:00 am:
# $ crontab -e
# 0 10 * * 3 /home/helen/projects/rand_and_send/script.sh

# sources the virtual environment needed to run the program
source /home/helen/projects/rand_and_send/venv/bin/activate

# moves into project directory
cd /home/helen/projects/rand_and_send

# turns to executable
chmod +x /home/helen/projects/rand_and_send/rand_and_send.py

# runs the program
/home/helen/projects/rand_and_send/rand_and_send.py

# deactivates the virtual environment
deactivate
