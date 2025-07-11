from gtts import gTTS
import os

def generate_audio(script_path, output_path, lang="en", slow=False):
    try:
        # Ensure output folder exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(script_path, "r") as file:
            text = file.read()
            if not text.strip():
                raise ValueError(f"No text found in script file: {script_path}")

        tts = gTTS(text=text, lang=lang, slow=slow)
        tts.save(output_path)
        print(f"✅ Audio narration saved: {output_path}")
    except Exception as e:
        print(f"❌ Error generating audio: {e}")
