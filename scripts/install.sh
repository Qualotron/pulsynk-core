#!/bin/bash

# Check if run with root rights
if [ "$EUID" -ne 0 ]
  then echo "[!] Please run as root"
  exit
fi

# Create service user / System User - No Home - No Login
user_exists(){ id -u "$1" &>/dev/null; } 
if user_exists pulsynk-core; then 
    echo 'User pulsynk-core already exists'
else
    sudo useradd -r -M -s /usr/sbin/nologin pulsynk-core
    echo "[*] User pulsynk-core created"
fi

# Create etc directories needed
if [ -d "/etc/pulsynk-core" ]; then
    echo "[?] Directory /etc/pulsynk-core/ already exists"
else
    sudo mkdir /etc/pulsynk-core
    echo "[*] Directory /etc/pulsynk-core/ created"
fi

sudo chown -R pulsynk-core:pulsynk-core /etc/pulsynk-core

# Copy config directory
if [ -d "../config" ]; then
    if [ -d "/etc/pulsynk-core/config" ]; then
        echo "[?] Files at /etc/pulsynk-core/config already exist"
    else
        sudo cp -r ../config /etc/pulsynk-core/config
        echo "[*] Config files copied"
    fi
else
    echo "[!] Could not find config files"
    exit
fi

# Copy whole project
if [ -d "../src" ]; then
    if [ -d "/etc/pulsynk-core/src" ]; then
        echo "[?] Files at /etc/pulsynk-core/src already exist"
    else
        sudo cp -r ../src /etc/pulsynk-core/src
        sudo chmod +x /etc/pulsynk-core/src/main.py
        echo "[*] Src created"
    fi
else
    echo "[!] Could not find src files"
    exit
fi

# Create Python venv
if [ -d "/etc/pulsynk-core/venv" ]; then
    echo "[!] Venv already exists"
else
    echo "[*] Creating python venv"
    sudo python3 -m venv /etc/pulsynk-core/venv
    sudo chown -R pulsynk-core:pulsynk-core /etc/pulsynk-core/venv
    echo "[*] venv created"
fi

# Configure Service
if [ -f "../systemd/pulsynk-core.service" ]; then
    if [ -f "/etc/systemd/system/pulsynk-core.system" ]; then
        echo "[?] File /etc/systemd/system/pulsynk-core.service already exists"
    else
        sudo cp ../systemd/pulsynk-core.service /etc/systemd/system
        echo "[*] File /etc/systemd/system/pulsynk-core.service created"
    fi
else
    echo "[!] Source file for pulsynk-core.service does not exist"
    exit
fi

# Copy requirements to project directory
if [ -f "../requirements.txt" ]; then
    if [ -d "/etc/pulsynk-core/requirements.txt" ]; then
        echo "[?] Files at /etc/pulsynk-core/requirements.txt already exist"
    else
        sudo cp ../requirements.txt /etc/pulsynk-core/requirements.txt
        echo "[*] Requirements file copied"
    fi
else
    echo "[!] Could not find requirements.txt file"
    exit
fi

# Change ownership of folder
sudo chown -R pulsynk-core:pulsynk-core /etc/pulsynk-core

# Install package dependencies
echo "[*] Installing dependencies"
sudo apt install python3-dev -y

# Install pip requirements
echo "[*] Installing pip requirements"
sudo /etc/pulsynk-core/venv/bin/pip3 install -r /etc/pulsynk-core/requirements.txt

# Reload and enable/start service
sudo systemctl daemon-reload
sudo systemctl enable pulsynk-core
sudo systemctl start pulsynk-core
