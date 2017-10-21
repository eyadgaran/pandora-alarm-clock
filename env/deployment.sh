# Deployment script for Pandora Alarm

# System Dependencies
sudo apt-get update
sudo apt-get install bzip2
sudo apt-get install unzip

# Install Conda (Assumes 64bit Linux)
cd /tmp
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest-Linux-x86_64.sh -f

# Install Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install

# Install Environment
cd ${HOME}/code-base/Python/Pandora-Alarm/env
conda env create -n pandora_alarm -f linux_requirements.yaml

# Install custom utilities package
source ${HOME}/.bash_profile
source activate pandora_alarm
cd ~/code-base/Python/packaged_scripts
python setup.py develop

# Chromedriver
wget https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip
unzip chromedriver_linux64.zip

# Create Log Directory
cd ${HOME}/code-base/Python/Pandora-Alarm/
mkdir logs

# Edit Cronjob
crontab -e

# Add Secrets File
cd scripts
nano secrets.py