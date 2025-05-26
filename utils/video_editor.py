import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

def edit_video(video_path, start=0, end=10, output_path='edited.mp4'):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file does not exist: {video_path}")

    try:
        clip = VideoFileClip(video_path)
        duration = clip.duration

        # Sanity check on subclip range
        if start >= end or start >= duration:
            raise ValueError(f"Invalid subclip range: start={start}, end={end}, video duration={duration}")

        end = min(end, duration)  # Ensure we don’t go past actual video duration

        edited = clip.subclipped(start, end)
        edited.write_videofile(output_path, codec='libx264')

        return output_path
    finally:
        # Always clean up to save space
        try:
            os.remove(video_path)
            print(f"🧹 Deleted original video: {video_path}")
        except Exception as e:
            print(f"⚠️ Could not delete video: {e}")
