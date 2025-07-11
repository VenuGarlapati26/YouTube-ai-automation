import os

def save_script(script, filename):
    try:
        os.makedirs("data/scripts", exist_ok=True)
        full_path = os.path.join("data/scripts", filename)
        with open(full_path, "w", encoding="utf-8") as file:
            file.write(script)
        print(f"✅ Script saved to {full_path}")
    except Exception as e:
        print(f"❌ Error saving script to {filename}: {e}")

def load_script(filename):
    try:
        full_path = os.path.join("data/scripts", filename)
        with open(full_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"❌ Error loading script from {filename}: {e}")
        return None
