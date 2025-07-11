import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_daily_scripts():
    try:
        short_prompt = "Generate a short script for a 30-second video on a trending topic."
        long_prompt = "Generate a detailed script for a 10-minute video on a trending topic."

        short_script_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": short_prompt}],
            max_tokens=300
        )
        long_script_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": long_prompt}],
            max_tokens=1200
        )

        short_script = short_script_response.choices[0].message.content.strip()
        long_script = long_script_response.choices[0].message.content.strip()

        return short_script, long_script
    except Exception as e:
        print(f"❌ Error generating scripts: {e}")
        return None, None
