# Cub3D Controled by hand Project - README

[
![VideoCapture_20240709-000446](https://github.com/eyubech/cub3d_handcontrol/assets/76597998/c4e263ca-6481-4586-a1f7-0bf34d3c0bc2)
](url)
## Overview


Hand Gesture Recognition for Automated Key Pressing
Project Overview
This project aims to develop a real-time hand gesture recognition system using a webcam to detect the number of fingers shown and automatically send corresponding key press signals to control other applications. The primary use case is to enhance user interaction in various scenarios, such as gaming, presentations, and assistive technologies.

## Key Features

Real-Time Hand Detection: Utilizes OpenCV for capturing video frames from a webcam and processing these frames to detect hand gestures in real-time.
Finger Counting: Employs image processing techniques to count the number of fingers displayed and triggers specific actions based on the count.
Automated Key Pressing: Integrates with xdotool to send key press signals, automating responses to specific hand gestures.
Configurable Key Bindings: Customizes actions for different finger counts, allowing flexibility in controlling various applications.

## Technologies Used

- OpenCV: An open-source computer vision library used for image processing, capturing video frames, and detecting hand gestures.
- NumPy: A library for numerical operations, used here for calculations related to finger counting.
- xdotool: A Linux command-line tool for simulating keyboard and mouse input, used to automate key presses based on detected gestures.

## Installation and Setup
### Prerequisites
- Python 3
- Webcam
-  Linux environment (for xdotool)
- Installing Dependencies
- opencv-python
- numpy

### Install the required Python libraries:

```sh
    pip install -r requirements.txt
```

```sh
    sudo apt-get install xdotool
```
```sh
    python3 hand_gesture_recognition.py
```
Ensure your target application cub3d_bonus is active and focused.

### Show gestures to the webcam:

- 2 Fingers: Sends the key press signal for key code 83.
- 3 Fingers: Sends the s key press.
- 4 Fingers: Sends the right arrow key press.
- 5 Fingers: Sends the left arrow key press.




## CUB3D AND MLX


- [cub3d](https://github.com/eyubech/cub3d)
- [MLX CODAM](https://github.com/codam-coding-college/MLX42)



## Contributing


Fork the repository.
Create your feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Create a new Pull Request.


##  License



This project is licensed under the MIT License - see the LICENSE file for details.


## View
[
![20240709_001504](https://github.com/eyubech/cub3d_handcontrol/assets/76597998/88fb8d21-27b8-4206-bf24-a3c0c7fdfaaf)
](url)




