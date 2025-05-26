from utils.video_fetcher import fetch_and_download_video
from utils.video_editor import edit_video

def main():
    keyword = input("Enter a keyword: ").strip()

    video_path = fetch_and_download_video(keyword, output_path='video.mp4')
    print(f"✅ Downloaded to: {video_path}")

    try:
        edited = edit_video(video_path, start=0, end=10, output_path='edited.mp4')
        print(f"🎞 Saved edited clip to: {edited}")
    except Exception as e:
        print(f"❌ Error editing video: {e}")

if __name__ == '__main__':
    main()