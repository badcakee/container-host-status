#!/bin/bash
set -e

apt update -y
apt install -y python3 python3-pip
pip3 install --upgrade pip
pip3 install psutil requests flask discord.py

curl -L -o monitor.py https://raw.githubusercontent.com/badcakee/container-host-status/main/monitor.py

read -p "Enter your Discord webhook URL: " WEBHOOK
sed -i "s|WEBHOOK_URL = .*|WEBHOOK_URL = \"$WEBHOOK\"|g" monitor.py

curl -L -o run.sh https://raw.githubusercontent.com/badcakee/container-host-status/refs/heads/main/idk/run.sh

echo -e "[Unit]\nDescription=Run custom script at startup\nAfter=network.target\n\n[Service]\nType=simple\nExecStart=/path/to/run.sh\nRestart=on-failure\n\n[Install]\nWantedBy=multi-user.target" | tee /etc/systemd/system/run-script.service > /dev/null

bash run.sh
