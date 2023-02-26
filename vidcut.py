import pytube
import requests
from colorama import Fore, init
from moviepy.editor import AudioFileClip, VideoFileClip

init(autoreset=True)
print("© 2023 anekobtw")
CURRENT_VERSION = "v1.2"

def check_for_updates(current_version):
    api_url = 'https://api.github.com/repos/anekobtw/youtube-clip-maker/releases/latest'
    latest_version = requests.get(api_url).json()['tag_name']
    if latest_version != current_version:
        print(f"{Fore.RED}\nYou are using an old version of the app. A new version is already available here:\
                            \nhttps://github.com/anekobtw/youtube-clip-maker\
                            \nLatest Version: {latest_version}\n")

def download_video(link):
    youtube = pytube.YouTube(link)
    youtube.streams.filter(only_audio=True).first().download(filename="audio.mp3")
    youtube.streams.filter(res="1080p").first().download(filename="video_without_audio.mp4")

def cut_video(start_time, end_time):
    video_cutted = VideoFileClip("video_without_audio.mp4").subclip(start_time, end_time)
    audio_cutted = AudioFileClip("audio.mp3").subclip(start_time, end_time)
    video_cutted.set_audio(audio_cutted).write_videofile("cutted_video.mp4", logger=None)

if __name__ == '__main__':
    check_for_updates(CURRENT_VERSION)
    if input("Download video/stream? (yes/no) ").lower() in ["yes", "y"]:
        download_video(input("Enter video link: "))
    cut_video(float(input("Enter clip start time: ")), float(input("Enter clip end time: ")))

    print("Done!")
    input("Press Enter to exit ")
