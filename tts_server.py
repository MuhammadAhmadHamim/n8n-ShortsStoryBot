from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    data = request.json
    text = data.get('text', '')
    output_file = 'path/to/your/outputFile.mp3'
    
    os.makedirs('path/to/folder/just before/outputFile/', exist_ok=True)
    
    subprocess.run([
        'edge-tts',
        '--text', text,
        '--voice', 'en-US-GuyNeural',
        '--write-media', output_file
    ])
    
    return jsonify({
        'status': 'success',
        'audio_path': output_file
    })

if __name__ == '__main__':
    app.run(port=5001)