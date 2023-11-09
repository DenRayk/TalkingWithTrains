# TalkingWithTrains

## Project Overview
This project is a part of a student research initiative at DHBW Karlsruhe aimed at implementing a speech control system for the DHBW Modellbahnanlage. The DHBW Modellbahnanlage is a model train system used for educational and recreational purposes within the university. The objective of this research project is to enhance the user experience and accessibility of the model train system by enabling it to be controlled through voice commands.

## Features
- **Voice Commands**: Users can control various aspects of the model train system by issuing voice commands, such as starting and stopping trains, changing track directions, controlling speed, and more.
- **Real-time Feedback**: The system provides real-time feedback to users, confirming the execution of commands and notifying them of any issues or errors.

## Getting Started
To get started with the speech control system for the DHBW Modellbahnanlage, follow these steps:

**1. Clone the Repository:**

```bash
git clone https://github.com/DenRayk/TalkingWithTrains.git
```

**2. Install Dependencies:**

Make sure you have Python 3.x installed on your system. You can install project-specific dependencies by running:

```bash
pip install -r requirements.txt
```

**3. Install ffmpeg:**

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman - ffmpeg

# on MacOS using Homebrew (https://brew.sh/) 
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/) 
scoop install ffmpeg
```

**4. Run the Code:**

Run the main script to start the speech control system:

```bash
python main.py
```
The system will begin listening for voice commands. Speak clearly and wait for the system's responses.

## Dependencies
- Python 3.11.6
- SpeechRecognition 3.10.0
- PyAudio 0.2.13
