from pytube import YouTube 
from moviepy.editor import AudioFileClip, VideoFileClip
print("© 2023 Aneko")

def download_video(link):
    YouTube(link).streams.filter(only_audio=True).first().download(filename="audio.mp3")
    YouTube(link).streams.filter(res="1080p").first().download(filename="video_without_audio.mp4")

def cut_video(start_time, end_time):
    video_cutted = VideoFileClip("video_without_audio.mp4").subclip(start_time, end_time)
    audio_cutted = AudioFileClip("audio.mp3").subclip(start_time, end_time)
    final_video = video_cutted.set_audio(audio_cutted)
    final_video.write_videofile("cutted_video.mp4", logger=None)

if __name__ == '__main__':
    if input("Download video/stream? (yes/no)   ") in ["yes", "y", "YES", "Yes"]:
        download_video(input("Enter video link: "))
    cut_video(input("Enter clip start time: "), input("Enter clip end time: "))

    print("Done!")
    input("Press Enter to exit ")
