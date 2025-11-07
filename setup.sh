#!/bin/bash

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "Downloading YOLO configuration and weights..."
python3 download_yolo.py
