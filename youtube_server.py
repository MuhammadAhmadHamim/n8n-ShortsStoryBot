from flask import Flask, request, jsonify
import os
import json
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

app = Flask(__name__)

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
CREDENTIALS_FILE = "path/to/credentials.json"
TOKEN_FILE = "path/to/token.pickle"
def get_youtube_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except:
                os.remove(TOKEN_FILE)
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(
                    port=0,
                    access_type='offline',
                    prompt='consent'
                )
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(
                port=0,
                access_type='offline',
                prompt='consent'
            )
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return build('youtube', 'v3', credentials=creds)

@app.route('/upload', methods=['POST'])
def upload_video():
    try:
        data = request.get_json(force=True, silent=True)
        if data is None:
            data = json.loads(request.data.decode('utf-8'))
        if isinstance(data, str):
            data = json.loads(data)
    except:
        data = {}
    
    print(f"Received data: {data}")
    video_path = data.get('video_path', 'path/to/your/outputFile.mp4')
    title = data.get('title', 'Amazing Story #Shorts')
    description = data.get('description', '')
    tags = data.get('tags', '').split(',')

    print(f"Title: {title}")
    print(f"Description: {description}")

    try:
        youtube = get_youtube_service()

        body = {
            'snippet': {
                'title': title,
                'description': description + '\n\n🎯 Follow for daily stories → link of your choice',
                'tags': tags,
                'categoryId': '24'
            },
            'status': {
                'privacyStatus': 'public',
                'selfDeclaredMadeForKids': False
            }
        }

        media = MediaFileUpload(
            video_path,
            mimetype='video/mp4',
            resumable=True
        )

        upload_response = youtube.videos().insert(
            part=','.join(body.keys()),
            body=body,
            media_body=media
        ).execute()

        video_id = upload_response.get('id')
        video_url = f"https://youtube.com/shorts/{video_id}"

        return jsonify({
            'status': 'success',
            'video_id': video_id,
            'video_url': video_url
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

if __name__ == '__main__':
    app.run(port=5003)