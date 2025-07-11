# generate_env.py
env_content = "OPENAI_API_KEY=your_api_key_here\n"

with open(".env", "w") as f:
    f.write(env_content)

print(".env file has been created with placeholder API key.")
