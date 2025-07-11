import os
import pickle
import logging
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CLIENT_SECRETS_FILE = "client_secrets.json"
TOKEN_FILE = "token.pickle"

def get_authenticated_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "wb") as token:
            pickle.dump(creds, token)

    return build("youtube", "v3", credentials=creds)

def upload_to_youtube(video_path, video_type, title=None, thumbnail_path=None):
    try:
        youtube = get_authenticated_service()

        # Default titles
        if not title:
            title = f"{video_type.capitalize()} Video - Auto Generated"
        description = f"This is an auto-generated {video_type} video created by an AI automation pipeline."

        request_body = {
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["AI", "automation", "YouTube", video_type],
                "categoryId": "22",  # Category ID 22 = People & Blogs
            },
            "status": {
                "privacyStatus": "public",
                "selfDeclaredMadeForKids": False,
            },
        }

        media_file = MediaFileUpload(video_path, mimetype="video/mp4", resumable=True)
        upload_request = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media_file
        )
        response = upload_request.execute()
        print(f"✅ Uploaded to YouTube: https://www.youtube.com/watch?v={response['id']}")

        # Upload thumbnail if provided
        if thumbnail_path and os.path.exists(thumbnail_path):
            youtube.thumbnails().set(
                videoId=response["id"],
                media_body=MediaFileUpload(thumbnail_path)
            ).execute()
            print(f"✅ Thumbnail uploaded for video ID: {response['id']}")

    except Exception as e:
        print(f"❌ Error uploading to YouTube: {e}")
