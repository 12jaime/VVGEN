from utils.video_fetcher import fetch_and_download_videos
from utils.video_editor import edit_video

def main():
    keyword = input("Enter a keyword: ").strip()

    videos_path = fetch_and_download_videos(keyword, output_dir='videos/')
    print(f"✅ Downloaded to: {video_path}")

    try:
        edited = edit_video(videos_path, start=0, end=10, output_dir='edited-videos/')
        print(f"🎞 Saved edited clip to: {edited}")
    except Exception as e:
        print(f"❌ Error editing video: {e}")

if __name__ == '__main__':
    main()