#!/bin/bash

echo "[🔧] Initializing SQLi Detection Platform..."

# Step 1: Install Python dependencies
echo "[📦] Installing Python packages..."
pip install -r requirements.txt

# Step 2: Initialize MySQL
echo "[🧩] Setting up MySQL database..."
mysql -u root -p < database/init.sql

# Step 3: Launch Flask app
echo "[🚀] Launching Flask web server at http://127.0.0.1:5000"
gnome-terminal -- bash -c "python app/server.py; exec bash"

# Step 4: Launch live detection monitor
echo "[👁️] Launching Burp SQLi detector monitor..."
gnome-terminal -- bash -c "python burpsuite/bridge_detector.py; exec bash"

echo "[✅] Done! Web server and monitor are live."
