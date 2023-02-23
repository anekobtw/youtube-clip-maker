from moviepy.editor import VideoFileClip, CompositeVideoClip
from enum import Enum

class Position(Enum):
    LEFT = 1
    RIGHT = 2
    CENTER = 3

def create_short():
    # Load the original video
    video = VideoFileClip("cutted_video.mp4")

    # Resize the video to 1080x1920 (9:16 aspect ratio)
    resized_video = video.resize(height=1080, width=608).crop(x1=144, y1=0, x2=752, y2=1080)

    # Set the position of the resized video
    position_input = input("Choose the position:\n1. left\n2. right\n3. center\n")
    position = Position(int(position_input))

    if position == Position.LEFT:
        resized_video = resized_video.set_position((0, 'center'))
    elif position == Position.RIGHT:
        resized_video = resized_video.set_position(("center", 0))
    elif position == Position.CENTER:
        resized_video = resized_video.set_position(("center", "center"))
    else:
        raise ValueError("Invalid position input")

    # Create the final video
    final_video = CompositeVideoClip([resized_video])

    # Write the final video to a file
    final_video.write_videofile("short_video.mp4", fps=60)

    # Close the video clips
    video.close()
    resized_video.close()
    final_video.close()

if __name__ == '__main__':
    create_short()
    print("Done!")
