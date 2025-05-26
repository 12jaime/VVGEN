import whisper
import os
from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from config import OUTPUT_VIDEO_PATH

def generate_captions(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    captions = result['text']
    
    video = VideoFileClip(video_path)
    txt_clip = TextClip(captions, fontsize=24, color='white')
    txt_clip = txt_clip.set_position('bottom').set_duration(video.duration)
    video = CompositeVideoClip([video, txt_clip])
    
    output_path = os.path.join(OUTPUT_VIDEO_PATH, 'captioned_video.mp4')
    video.write_videofile(output_path, codec='libx264')
    return output_path
