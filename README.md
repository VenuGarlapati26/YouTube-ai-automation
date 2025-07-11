# 🎥 YouTube AI Automation – Version 1

This project is a **fully automated YouTube content generation pipeline** that uses **AI and Python** to create and upload videos without manual effort. It generates two types of videos daily:
- **Shorts (30–60 sec)**
- **Long-form videos (~10 min)**

> Ideal for educational, fact-based, or infotainment content targeting all age groups.

---

## 🚀 Features

- 🧠 **AI-Powered Script Generation** using OpenAI GPT-4o
- 🎙️ **Text-to-Speech (TTS)** voice narration with gTTS fallback if ElevenLabs fails
- 🎬 **Video Creation** using MoviePy with dynamic text overlays
- 🎵 **Audio Integration** with background music
- 🖼️ **Automatic Thumbnail Generation** using Pillow
- ⏰ **Daily Automation** via local scheduling (macOS `cron`)
- 📤 **Auto Upload** to YouTube using YouTube Data API v3
- 🧾 **Upload Logging** (tracks uploaded video IDs & timestamps)
- 🔒 **Secrets management** with `.env` and `.gitignore`

---

## 🧠 Technologies Used

| Category               | Tools / Libraries                                |
|------------------------|--------------------------------------------------|
| Language               | Python 3.10                                       |
| AI Model               | OpenAI GPT-4o                                     |
| Video Editing          | [MoviePy](https://zulko.github.io/moviepy/)     |
| Text-to-Speech         | gTTS (fallback), ElevenLabs (optional)           |
| Audio/Video Handling   | imageio, imageio-ffmpeg, Pillow                   |
| YouTube Integration    | google-api-python-client, oauth2client           |
| Scheduling             | `cron` (macOS)                                    |
| Environment Handling   | `python-dotenv`, `.env`                           |

---

## 📁 Folder Structure

```
youtube-ai-automation/
├── main.py                          # Entry point for daily pipeline
├── .env                             # Contains API keys (ignored by git)
├── .gitignore                       # Prevents secrets from being committed
├── requirements.txt                 # All Python dependencies
├── schedule.json                    # Optional upload schedule config
├── data/
│   ├── scripts/                     # AI-generated scripts
│   ├── audio/                       # Audio narration files
│   ├── videos/                      # Final generated videos
│   └── thumbnails/                 # Auto-generated thumbnails
└── utils/
    ├── content_generator.py         # OpenAI script generation
    ├── tts_engine.py                # gTTS/ElevenLabs audio generator
    ├── video_creator.py             # Create video clips from scripts
    ├── thumbnail_generator.py       # Create thumbnails using Pillow
    ├── uploader.py                  # Upload video & thumbnail to YouTube
    └── file_utils.py                # File save/load utilities
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/VenuGarlapati26/YouTube-ai-automation.git
cd YouTube-ai-automation
```

### 2. Create & Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Create Your `.env` File

```bash
touch .env
```

Then add your keys:

```
OPENAI_API_KEY=your-openai-api-key
```

### 5. Add Your YouTube Client Secret File

Place your `client_secrets.json` in the project root.  
**Do not commit this file to GitHub. It is ignored via `.gitignore`.**

---

## ▶️ Running the Pipeline

To run the full daily pipeline:

```bash
python main.py
```

---

## 🔐 Security

Sensitive files ignored via `.gitignore`:

```
.env
client_secrets.json
__pycache__/
*.pyc
*.pkl
*.log
*.db
```

---

## 👨‍💻 Maintainer

**Venu Garlapati**  
[LinkedIn](https://www.linkedin.com/in/venugarlapati/) • [GitHub](https://github.com/VenuGarlapati26)

---

## 📄 License

MIT License
