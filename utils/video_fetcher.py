import requests
import re
import yt_dlp
import os

def fetch_and_download_videos(keyword, max_videos=3, output_dir='videos'):
    os.makedirs(output_dir, exist_ok=True)

    # 1. Fetch video URLs from YouTube search
    query = keyword.replace(' ', '+')
    url = f'https://www.youtube.com/results?search_query={query}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch YouTube results (status: {response.status_code})")

    video_ids = []
    seen = set()
    for match in re.findall(r"watch\?v=(\w{11})", response.text):
        if match not in seen:
            video_ids.append(match)
            seen.add(match)
        if len(video_ids) >= max_videos:
            break

    if not video_ids:
        raise Exception("No video IDs found.")

    downloaded_files = []

    # 2. Download each video using yt-dlp
    for i, vid in enumerate(video_ids):
        video_url = f"https://www.youtube.com/watch?v={vid}"
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
