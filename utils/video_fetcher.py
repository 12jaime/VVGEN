import os
from googleapiclient.discovery import build
import yt_dlp

def fetch_and_download_videos(keyword, max_videos=3, output_dir='videos'):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Retrieve the API key from environment variables
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise Exception("❌ YOUTUBE_API_KEY environment variable not set.")

    # Build the YouTube API client
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Search for videos matching the keyword
    search_response = youtube.search().list(
        q=keyword,
        part='id',
        type='video',
        maxResults=max_videos
    ).execute()

    # Extract video IDs from the search response
    video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]
    if not video_ids:
        raise Exception("❌ No videos found for the given keyword.")

    downloaded_files = []

    # Download each video using yt_dlp
    for i, video_id in enumerate(video_ids):
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        output_path = os.path.join(output_dir, f'video_{i}.mp4')

        ydl_opts = {
            'format': 'bv*[ext=mp4]+ba[ext=m4a]/mp4',
            'merge_output_format': 'mp4',
            'outtmpl': output_path,
            'quiet': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"⬇️ Downloading: {video_url}")
            ydl.download([video_url])

        downloaded_files.append(output_path)

    return downloaded_files
