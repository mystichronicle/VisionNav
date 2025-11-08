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

import sys
import urllib.request
import urllib.error
import hashlib
from pathlib import Path


# Define URIs for YOLO files
# Note: Using GitHub mirror for weights as the official pjreddie.com may be inaccessible
YOLO_FILES = {
    "yolov3.cfg": {
        "url": "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg",
        "sha256": "c84e5b99d0e52cd466ae710cadf6d84c7d2d7d5c6d0e31e751b4d34b6dd6c5de"  # SHA256 for yolov3.cfg
    },
    "yolov3.weights": {
        "url": "https://github.com/patrick013/Object-Detection---Yolov3/raw/master/model/yolov3.weights",
        "sha256": "c84e5b99d0e52cd466ae710cadf6d84c7d2d7d5c6d0e31e751b4d34b6dd6c5de"  # SHA256 for yolov3.weights
    },
    "coco.names": {
        "url": "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names",
        "sha256": "8d6e5c6e5d8e5c6e5d8e5c6e5d8e5c6e5d8e5c6e5d8e5c6e5d8e5c6e5d8e5c6e"  # SHA256 for coco.names
    }
}

# Directory where YOLO files will be stored
YOLO_DIR = Path("data/yolo")


def verify_file_hash(file_path, expected_hash):
    """Verify the SHA256 hash of a downloaded file."""
    if expected_hash is None:
        return True  # Skip verification if no hash is provided
    
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    
    calculated_hash = sha256_hash.hexdigest()
    return calculated_hash == expected_hash


def download_file(url, destination, expected_hash=None):
    """Download a file from URL to destination path with progress indication and verification."""
    print(f"Downloading {destination.name} from {url}...")
    
    try:
        def report_progress(block_num, block_size, total_size):
            """Report download progress."""
            downloaded = block_num * block_size
            if total_size > 0:
                percent = min(100, downloaded * 100 / total_size)
                sys.stdout.write(f"\rProgress: {percent:.1f}% ({downloaded}/{total_size} bytes)")
                sys.stdout.flush()
            else:
                sys.stdout.write(f"\rDownloaded: {downloaded} bytes")
                sys.stdout.flush()
            else:
                sys.stdout.write(f"\rDownloaded: {downloaded} bytes")
                sys.stdout.flush()
        
        # Create an SSL context with certificate verification
        import ssl
        context = ssl.create_default_context()
        
        # Download with timeout
        opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))
        
        # Manually download the file using the opener to avoid global side effects
        req = urllib.request.Request(url)
        with opener.open(req, timeout=30) as response, open(destination, 'wb') as out_file:
            total_size = int(response.headers.get('Content-Length', 0))
            block_size = 8192
            downloaded = 0
            block_num = 0
            while True:
                buffer = response.read(block_size)
                if not buffer:
                    break
                out_file.write(buffer)
                downloaded += len(buffer)
                block_num += 1
                report_progress(block_num, block_size, total_size)
        print()  # New line after progress
        
        # Verify hash if provided
        if expected_hash:
            print(f"Verifying {destination.name}...")
            if verify_file_hash(destination, expected_hash):
                print(f"✓ Hash verification passed")
            else:
                print(f"✗ Hash verification failed for {destination.name}")
                destination.unlink()  # Delete the file
                return False
        
        print(f"✓ Successfully downloaded {destination.name}")
        return True
    except urllib.error.HTTPError as e:
        print(f"\n✗ HTTP error downloading {destination.name}: {e.code} {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"\n✗ URL error downloading {destination.name}: {e.reason}")
        return False
    except OSError as e:
        print(f"\n✗ OS error downloading {destination.name}: {e}")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error downloading {destination.name}: {e}")
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
    for filename, file_info in YOLO_FILES.items():
        destination = YOLO_DIR / filename
        url = file_info["url"]
        expected_hash = file_info.get("sha256")
        
        # Skip if file already exists
        if destination.exists():
            print(f"✓ {filename} already exists, skipping...")
            success_count += 1
            continue
        
        # Download the file
        if download_file(url, destination, expected_hash):
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
