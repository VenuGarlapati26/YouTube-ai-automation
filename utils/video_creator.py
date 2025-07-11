import os
from moviepy.editor import TextClip, concatenate_videoclips, AudioFileClip
from utils.file_utils import load_script

def create_video(script_path, video_type, audio_path):
    try:
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"Script file not found: {script_path}")
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")

        os.makedirs("data/videos", exist_ok=True)

        script = load_script(os.path.basename(script_path))
        if not script or not script.strip():
            raise ValueError(f"No text found in script file: {script_path}")

        lines = script.split("\n")
        clips = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            duration = max(3, len(line) / 10)
            txt_clip = TextClip(
                line,
                fontsize=50,
                color='white',
                bg_color='black',
                size=(1920, 1080),
                font="Helvetica"  # Or "Arial"
            ).set_duration(duration)
            clips.append(txt_clip)

        video = concatenate_videoclips(clips)
        audio = AudioFileClip(audio_path)
        video = video.set_audio(audio)

        output_filename = f"{video_type}_{os.path.basename(script_path).replace('.txt', '.mp4')}"
        output_path = os.path.join("data/videos", output_filename)

        video.write_videofile(output_path, fps=24)
        print(f"✅ Video saved to: {output_path}")

        return output_path
    except Exception as e:
        print(f"❌ Error in create_video: {e}")
        return None
