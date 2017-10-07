#!/bin/bash
PROJECT='Pandora-Alarm'
LOGFILE=~/documents/scripts/Python/$PROJECT/logs/logfile.log

touch "$LOGFILE"

source ~/.bash_profile
source activate pandora_alarm
python ~/documents/scripts/Python/$PROJECT/scripts/echo_player.py >> "$LOGFILE" 2>&1
source deactivate
