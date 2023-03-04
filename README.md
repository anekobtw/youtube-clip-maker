# YouTube Clip Maker v1.3
This Python script downloads a video from YouTube, extracts its audio, cuts a section of the video and then merges the cutted video with the extracted audio to create a new video file. It uses the `pytube` and `moviepy` libraries to achieve this.

## Installation
Clone this repository to your local machine or download the ZIP file and extract it.\
Install the required packages using `pip install -r requirements.txt`.

Notice that python must be installed on your computer.

## Usage
1. When prompted, enter the video link you want to download from YouTube.
2. Enter the start and end times for the section of the video you want to cut (in seconds).
3. The script will then download the video, extract its audio, cut the section of the video and merge the cutted video with the extracted audio to create a new video file called cutted_video.mp4.

Note: You can skip the video download step if you already have the video file downloaded on your computer. Just make sure the video file is in the same directory as the script and rename it to `video.mp4`.

## License
This project is licensed under the MIT license.
