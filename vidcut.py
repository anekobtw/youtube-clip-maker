import os
from moviepy.editor import AudioFileClip, VideoFileClip
from pytube import YouTube 

def download_video(link: str):
    # Download audio
    audio = YouTube(link).streams.filter(only_audio=True)[0].download()
    os.rename(audio, "audio.mp3")

    # Download video
    video = YouTube(link).streams.filter(res="1080p").first().download() 
    os.rename(video, "video.mp4")  

def cut_video(start_time: float, end_time: float):
    # Cut video
    video = VideoFileClip("video.mp4")
    video.subclip(start_time, end_time).write_videofile("video_cutted.mp4")
    video.close()
    os.remove("video.mp4")

    # Cut audio
    audio = AudioFileClip("audio.mp3")
    audio.subclip(start_time, end_time).write_audiofile("audio_cutted.mp3")
    audio.close()
    os.remove("audio.mp3")

def combine():
    # Combine video and audio
    video = VideoFileClip("video_cutted.mp4")
    audio = AudioFileClip("audio_cutted.mp3")
    final_video = video.set_audio(audio)
    final_video.write_videofile("video.mp4")

    video.close()
    os.remove("video_cutted.mp4")

    audio.close()
    os.remove("audio_cutted.mp3")

if __name__ == '__main__':
    link = input("Enter video link: ")
    start_time = float(input("Enter start time (in seconds): "))
    end_time = float(input("Enter end time (in seconds): "))

    download_video(link)
    cut_video(start_time, end_time)
    combine()

    print("Done!")

    input("Press Enter to exit ")
