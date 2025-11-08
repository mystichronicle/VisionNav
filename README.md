
# VisionNav

![image](https://github.com/user-attachments/assets/6b2de43a-e4a1-4c49-99f2-005425f23ac4)

VisionNav is a cutting-edge navigation system designed for visually impaired individuals, providing real-time guidance through voice commands. The system leverages advanced technologies such as OpenCV, SLAM, YOLO for object detection, and Text-to-Speech (TTS) to recognize indoor landmarks and obstacles, ensuring precise and safe navigation.

## Features

- **Real-Time Object Detection and Recognition:** Utilizes YOLO to detect and recognize objects in the environment.
- **Indoor Localization and Mapping:** Employs SLAM (Simultaneous Localization and Mapping) to create and update maps in real-time.
- **Voice Guidance:** Provides audio feedback and navigation commands using Text-to-Speech.
- **Multi-Floor Navigation:** Supports navigation across multiple floors with elevator recognition.
- **Bluetooth Beacon Integration:** Enhances indoor positioning accuracy using Bluetooth beacons.

## Technologies Used

- **OpenCV:** For capturing and processing video feed.
- **SLAM:** For real-time localization and mapping.
- **YOLO:** For object detection.
- **Text-to-Speech (pyttsx3):** For voice guidance.
- **Bleak:** For Bluetooth beacon integration.
- **Python:** The primary programming language used.

## Setup

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/debjit-mandal/VisionNav.git
    cd VisionNav
    ```

2. **Install the required dependencies and download YOLO files:**

    The setup script will install dependencies and automatically download YOLO configuration and weights:

    ```bash
    ./setup.sh
    ```

    Alternatively, you can download YOLO files manually:

    ```bash
    python3 download_yolo.py
    ```

    The download script uses the following URIs:
    - Config: `https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg`
    - Weights: `https://github.com/patrick013/Object-Detection---Yolov3/raw/master/model/yolov3.weights`
    - Names: `https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names`

3. **Collect Bluetooth beacon data (if applicable):**

    ```bash
    python collect_beacon_data.py
    ```

### Running the Application

1. **Run the main script:**

    ```bash
    python -m src.main
    ```

2. **Usage:**

    - The system will start capturing video from the webcam.
    - Detected objects will be displayed with bounding boxes and labels.
    - Voice commands will guide the user based on detected objects and navigation logic.
    - Bluetooth beacon data will be printed after the video feed is stopped.

## Directory Structure

- `data/`: Contains configuration files and data.
  - `beacons/`: Stores Bluetooth beacon data.
  - `yolo/`: Contains YOLO configuration, weights, and class names.
- `src/`: Contains source code for object detection, SLAM, navigation, TTS, and Bluetooth integration.
  - `main.py`: Main script to run the application.
  - `object_detection.py`: Module for object detection using YOLO.
  - `tts.py`: Module for Text-to-Speech functionality.
  - `slam.py`: Module placeholder for SLAM functionality.
  - `navigation.py`: Module for navigation logic.
  - `bluetooth.py`: Module for Bluetooth beacon integration.
- `requirements.txt`: List of dependencies.
- `setup.sh`: Setup script to install dependencies.
- `README.md`: Project documentation.
- `LICENSE`: License for the project.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements, bug fixes, or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for providing the tools and libraries used in this project.
- Special thanks to the creators of OpenCV, YOLO, pyttsx3, and Bleak.

------------------------------------------------------------------------

Happy navigating!
