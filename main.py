from dotenv import load_dotenv
load_dotenv()

from datetime import datetime
import os
from utils.content_generator import generate_daily_scripts
from utils.file_utils import save_script
from utils.tts_engine import generate_audio
from utils.video_creator import create_video
from utils.uploader import upload_to_youtube
from utils.thumbnail_generator import generate_thumbnail


def daily_automation_pipeline():
    try:
        # Create necessary directories
        os.makedirs("data/scripts", exist_ok=True)
        os.makedirs("data/audio", exist_ok=True)
        os.makedirs("data/videos", exist_ok=True)
        os.makedirs("data/thumbnails", exist_ok=True)

        today = datetime.now().strftime("%Y-%m-%d")

        print("Step 1: Generating scripts...")
        short_script, long_script = generate_daily_scripts()
        if not short_script or not long_script:
            raise ValueError("Failed to generate scripts.")

        short_script_filename = f"short_{today}.txt"
        long_script_filename = f"long_{today}.txt"

        save_script(short_script, short_script_filename)
        save_script(long_script, long_script_filename)

        short_script_path = os.path.join("data/scripts", short_script_filename)
        long_script_path = os.path.join("data/scripts", long_script_filename)

        print("Step 2: Generating audio narration...")
        short_audio_path = f"data/audio/short_{today}_narration.mp3"
        long_audio_path = f"data/audio/long_{today}_narration.mp3"
        generate_audio(short_script_path, short_audio_path)
        generate_audio(long_script_path, long_audio_path)

        print("Step 3: Creating videos...")
        short_video_path = create_video(short_script_path, "short", short_audio_path)
        long_video_path = create_video(long_script_path, "long", long_audio_path)

        print("Step 4: Generating thumbnails...")
        short_title = "Short Video - Auto Generated"
        long_title = "Long Video - Auto Generated"
        short_thumb_path = f"data/thumbnails/short_{today}.jpg"
        long_thumb_path = f"data/thumbnails/long_{today}.jpg"
        generate_thumbnail("short", short_title, short_thumb_path)
        generate_thumbnail("long", long_title, long_thumb_path)

        print("Step 5: Uploading videos...")
        upload_to_youtube(short_video_path, "short", title=short_title, thumbnail_path=short_thumb_path)
        upload_to_youtube(long_video_path, "long", title=long_title, thumbnail_path=long_thumb_path)

        print("✅ Pipeline completed successfully!")
    except Exception as e:
        print(f"❌ Error in automation pipeline: {e}")


if __name__ == "__main__":
    daily_automation_pipeline()
