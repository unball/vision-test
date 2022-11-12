#/bin/env bash

cd /workspaces/vision-test
if ! [[ -d ".venv" ]]; then
    python3 -m venv .venv
fi

sudo apt update
sudo apt install libgl1-mesa-glx 

. .venv/bin/activate

if [[ -f "requirements.txt" ]]; then 
    pip3 install --user -r requirements.txt
fi