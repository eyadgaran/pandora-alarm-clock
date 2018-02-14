#!/bin/bash
PROJECT='pandora-alarm-clock'

LOGFILE=${HOME}/$PROJECT/logs/logfile.log
touch "$LOGFILE"

source ${HOME}/.bash_profile
source activate pandora_alarm
python ${HOME}/$PROJECT/scripts/echo_player.py >> "$LOGFILE" 2>&1
source deactivate
