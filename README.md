# AI_Exercices_counter
# Pose Analysis and Exercise Counter

![Demo](path_to_demo_gif_or_image.gif)

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a pose analysis and exercise counter using computer vision techniques with OpenCV, NumPy, and Mediapipe libraries. The program processes a video and tracks specific poses, calculates angles, and performs a curl counter for exercise analysis.

## Requirements

- Python (>=3.6)
- OpenCV (cv2)
- NumPy
- Mediapipe

## Installation

1. Clone the repository:

2. Install the required dependencies:

pip install -r requirements.tx

## Usage

1. Download the video you want to analyze and place it in the `trainvd` directory.

2. Update the video filename in the script:

  python
    cap = cv2.VideoCapture('trainvd/your_video.mp4')
Run the script:
  The program will process the video and display the analysis on the screen.

## How it Works
The program uses the Mediapipe library to detect pose landmarks from the video frames. It then calculates the angles between specific body landmarks to analyze the pose. Additionally, it performs a curl counter by tracking specific angles associated with the exercise.

https://github.com/MohamedAlaouiMhamdi/AI_Exercices_counter/assets/98537138/7a6fea43-bc5f-4712-a09f-4ac746f1062d

## Results
Include here any relevant screenshots, GIFs, or videos that showcase the project in action.

## Contributing
Contributions are welcome! If you find any issues or have ideas for improvements, please open an issue or create a pull request.

## License
This project is licensed under the MIT License.
