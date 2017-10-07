#!/bin/bash
PROJECT='Pandora-Alarm'
CODE_BASE=${HOME}/code-base

LOGFILE=$CODE_BASE/Python/$PROJECT/logs/logfile.log
touch "$LOGFILE"

source ${HOME}/.bash_profile
source activate pandora_alarm
python $CODE_BASE/Python/$PROJECT/scripts/echo_player.py >> "$LOGFILE" 2>&1
source deactivate
