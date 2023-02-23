import threading
from pytube import YouTube 
from moviepy.editor import AudioFileClip, VideoFileClip

def download_video(link: str):
    # Download audio and video
    def download_audio():
        YouTube(link).streams.filter(only_audio=True).first().download(output_path=".", filename="audio.mp3")

    def download_video():
        YouTube(link).streams.filter(res="1080p").first().download(output_path=".", filename="video.mp4")

    audio_thread = threading.Thread(target=download_audio)
    video_thread = threading.Thread(target=download_video)

    audio_thread.start()
    video_thread.start()

    audio_thread.join()
    video_thread.join()

def cut_video(start_time: float, end_time: float):
    video_cutted = VideoFileClip("video.mp4").subclip(start_time, end_time)
    audio_cutted = AudioFileClip("audio.mp3").subclip(start_time, end_time)

    final_video = video_cutted.set_audio(audio_cutted)
    final_video.write_videofile("cutted_video.mp4")

    video_cutted.close()
    audio_cutted.close()


if __name__ == '__main__':
    link = input("Enter video link: ")
    start_time = float(input("Enter start time (in seconds): "))
    end_time = float(input("Enter end time (in seconds): "))

    download_video(link)
    cut_video(start_time, end_time)

    print("Done!")
    input("Press Enter to exit ")
