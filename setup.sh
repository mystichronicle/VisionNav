#!/bin/bash

echo "Installing Python dependencies..."
python3 -m pip install -r requirements.txt

echo ""
echo "Downloading YOLO configuration and weights..."
python3 download_yolo.py
