import threading
from pytube import YouTube 
from moviepy.editor import AudioFileClip, VideoFileClip
print("© 2023, Aneko\n")

def download_video(link: str):
    print("Downloading...")

    def download_audio():
        YouTube(link).streams.get_by_itag(18).download(output_path=".", filename="audio.mp3")
        print("Audio has been downloaded.")

    def download_video():
        YouTube(link).streams.filter(res="1080p").first().download(output_path=".", filename="video.mp4")
        print("Video has been downloaded.")

    audio_thread = threading.Thread(target=download_audio)
    video_thread = threading.Thread(target=download_video)

    audio_thread.start()
    video_thread.start()

    audio_thread.join()
    video_thread.join()

    print("Download complete!")

def cut_video(start_time: float, end_time: float):
    print("Cutting...")

    video_cut = VideoFileClip("video.mp4").subclip(start_time, end_time)
    audio_cut = AudioFileClip("audio.mp3").subclip(start_time, end_time)

    final_video = video_cut.set_audio(audio_cut)
    final_video.write_videofile("cut_video.mp4", fps=60, logger=None)

    print("Video has been cut and saved as cut_video.mp4")

if __name__ == '__main__':
    print("Note: Make sure you have pytube and moviepy installed.")

    if input("Do you want to download a video (Y/n)? ").lower() in ["yes", "y"]:
        link = input("Enter video link: ")
        download_video(link)

    start_time = float(input("Enter Dtime (in seconds): "))
    end_time = float(input("Enter end time (in seconds): "))
    cut_video(start_time, end_time)

    print("Done!")
    input("Press Enter to exit ")
