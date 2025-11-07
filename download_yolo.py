#!/usr/bin/env python3
"""
Download YOLO configuration and weights files.

This script downloads the necessary YOLO v3 files:
- yolov3.cfg: Configuration file
- yolov3.weights: Pre-trained weights
- coco.names: Class names for COCO dataset

URIs for YOLO files:
- Config: https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg
- Weights: https://github.com/patrick013/Object-Detection---Yolov3/raw/master/model/yolov3.weights
- Names: https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names
"""

import os
import sys
import urllib.request
from pathlib import Path


# Define URIs for YOLO files
YOLO_FILES = {
    "yolov3.cfg": "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg",
    "yolov3.weights": "https://github.com/patrick013/Object-Detection---Yolov3/raw/master/model/yolov3.weights",
    "coco.names": "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"
}

# Directory where YOLO files will be stored
YOLO_DIR = Path("data/yolo")


def download_file(url, destination):
    """Download a file from URL to destination path with progress indication."""
    print(f"Downloading {destination.name} from {url}...")
    
    try:
        def report_progress(block_num, block_size, total_size):
            """Report download progress."""
            downloaded = block_num * block_size
            if total_size > 0:
                percent = min(100, downloaded * 100 / total_size)
                sys.stdout.write(f"\rProgress: {percent:.1f}% ({downloaded}/{total_size} bytes)")
                sys.stdout.flush()
        
        urllib.request.urlretrieve(url, destination, reporthook=report_progress)
        print(f"\n✓ Successfully downloaded {destination.name}")
        return True
    except Exception as e:
        print(f"\n✗ Error downloading {destination.name}: {e}")
        return False


def main():
    """Main function to download all YOLO files."""
    print("=" * 60)
    print("YOLO Configuration and Weights Downloader")
    print("=" * 60)
    print()
    
    # Create YOLO directory if it doesn't exist
    YOLO_DIR.mkdir(parents=True, exist_ok=True)
    print(f"YOLO files will be saved to: {YOLO_DIR.absolute()}")
    print()
    
    success_count = 0
    total_files = len(YOLO_FILES)
    
    # Download each file
    for filename, url in YOLO_FILES.items():
        destination = YOLO_DIR / filename
        
        # Skip if file already exists
        if destination.exists():
            print(f"✓ {filename} already exists, skipping...")
            success_count += 1
            continue
        
        # Download the file
        if download_file(url, destination):
            success_count += 1
        print()
    
    # Print summary
    print("=" * 60)
    print(f"Download Summary: {success_count}/{total_files} files ready")
    print("=" * 60)
    
    if success_count == total_files:
        print("✓ All YOLO files are ready!")
        return 0
    else:
        print("✗ Some files failed to download. Please check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
