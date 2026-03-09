from flask import Flask, request, jsonify
import requests
import subprocess
import os
import json as json_module
import threading

app = Flask(__name__)

PEXELS_API_KEY = "paste-your-pexels-key-here"

STORY_VISUALS = {
    "betrayal": "dramatic people shadows",
    "revenge": "determined person walking",
    "redemption": "sunrise person hope",
    "heartbreak": "sad person window rain",
    "life lesson": "person thinking reflection",
    "shocking twist": "dramatic cinematic moment",
    "motivational comeback": "person running success",
    "family": "family silhouette dramatic",
    "default": "cinematic dramatic people"
}

def get_visual_term(tags):
    tags_lower = tags.lower()
    for keyword, visual in STORY_VISUALS.items():
        if keyword in tags_lower:
            return visual
    return STORY_VISUALS["default"]

def generate_video_background(search_term, hook_text, audio_path, output_path, clips_dir):
    try:
        # Get audio duration
        probe = subprocess.run([
            'ffprobe', '-v', 'quiet',
            '-print_format', 'json',
            '-show_format',
            audio_path
        ], capture_output=True, text=True)

        audio_info = json_module.loads(probe.stdout)
        audio_duration = float(audio_info['format']['duration']) + 2
        duration_str = str(int(audio_duration))

        # Search and download clips
        headers = {"Authorization": PEXELS_API_KEY}
        clip_paths = []
        search_terms = [search_term, "cinematic people dramatic", "emotional moment people"]

        for term in search_terms:
            response = requests.get(
                f"https://api.pexels.com/videos/search?query={term}&per_page=3&orientation=portrait",
                headers=headers
            )
            videos = response.json().get('videos', [])

            for video in videos[:2]:
                video_files = video['video_files']
                hd_file = None
                for vf in video_files:
                    if vf.get('width', 0) <= 1080:
                        hd_file = vf
                        break
                if not hd_file:
                    hd_file = video_files[0]

                clip_url = hd_file['link']
                clip_path = f"{clips_dir}/clip_{len(clip_paths)}.mp4"

                clip_data = requests.get(clip_url, stream=True)
                with open(clip_path, 'wb') as f:
                    for chunk in clip_data.iter_content(chunk_size=8192):
                        f.write(chunk)
                clip_paths.append(clip_path)
                print(f"Downloaded clip {len(clip_paths)}")

        # Re-encode each clip to same format
        reencoded_paths = []
        for idx, clip_path in enumerate(clip_paths):
            reencoded_path = f"{clips_dir}/reencoded_{idx}.mp4"
            subprocess.run([
                'ffmpeg', '-y',
                '-i', clip_path,
                '-vf', 'scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,fps=30',
                '-c:v', 'libx264',
                '-preset', 'fast',
                '-crf', '23',
                '-pix_fmt', 'yuv420p',
                '-r', '30',
                reencoded_path
            ])
            reencoded_paths.append(reencoded_path)
            print(f"Re-encoded clip {idx + 1}")

        # Create concat file
        concat_file = f"{clips_dir}/concat.txt"
        with open(concat_file, 'w') as f:
            for cp in reencoded_paths:
                f.write(f"file '{cp}'\n")

        # Stitch all clips into one clean file
        once_path = f"{clips_dir}/once.mp4"
        subprocess.run([
            'ffmpeg', '-y',
            '-f', 'concat',
            '-safe', '0',
            '-i', concat_file,
            '-c:v', 'copy',
            once_path
        ])
        print("Clips stitched into once.mp4")

        # Loop stitched file to match audio duration
        stitched_path = f"{clips_dir}/stitched.mp4"
        subprocess.run([
            'ffmpeg', '-y',
            '-stream_loop', '-1',
            '-i', once_path,
            '-c:v', 'libx264',
            '-preset', 'fast',
            '-crf', '23',
            '-pix_fmt', 'yuv420p',
            '-t', duration_str,
            stitched_path
        ])
        print("Stitched file looped to match audio duration")

        # Clean hook text for FFmpeg
        safe_hook = hook_text.replace("'", "").replace(":", "").replace('"', "")
        line1 = safe_hook[:35]
        line2 = safe_hook[35:70]

        # Add audio + text overlays
        subprocess.run([
            'ffmpeg', '-y',
            '-i', stitched_path,
            '-i', audio_path,
            '-vf', (
                "colorize=hue=0:saturation=0:lightness=0.3,"
                f"drawtext=text='{line1}'"
                ":fontsize=48"
                ":fontcolor=white"
                ":borderw=3"
                ":bordercolor=black"
                ":x=(w-text_w)/2"
                ":y=150"
                ":enable='between(t,0,5)',"
                f"drawtext=text='{line2}'"
                ":fontsize=48"
                ":fontcolor=white"
                ":borderw=3"
                ":bordercolor=black"
                ":x=(w-text_w)/2"
                ":y=230"
                ":enable='between(t,0,5)',"
                "drawtext=text='WaterMark to add'"
                ":fontsize=32"
                ":fontcolor=white@0.7"
                ":borderw=2"
                ":bordercolor=black"
                ":x=(w-text_w)/2"
                ":y=h-100"
            ),
            '-c:v', 'libx264',
            '-preset', 'fast',
            '-crf', '23',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-map', '0:v:0',
            '-map', '1:a:0',
            '-movflags', '+faststart',
            '-shortest',
            output_path
        ])
        print("Final video created successfully")

    except Exception as e:
        print(f"Error generating video: {e}")

@app.route('/video', methods=['POST'])
def create_video():
    data = request.json
    raw_term = data.get('search_term', 'storytelling')
    hook_text = data.get('hook', '')
    search_term = get_visual_term(raw_term)
    audio_path = "path/to/your/outputFile.mp3"
    output_path = "path/to/your/outputFile.mp4"
    clips_dir = "path/to/folder/to save/clips"

    os.makedirs(clips_dir, exist_ok=True)
    os.makedirs("path/to/folder/just before/outputFile", exist_ok=True)

    # Clear old clips
    for old_clip in os.listdir(clips_dir):
        try:
            os.remove(os.path.join(clips_dir, old_clip))
        except:
            pass

    # Start video generation in background thread
    thread = threading.Thread(
        target=generate_video_background,
        args=(search_term, hook_text, audio_path, output_path, clips_dir)
    )
    thread.start()

    # Return immediately to n8n without waiting
    return jsonify({
        'status': 'processing',
        'video_path': output_path,
        'message': 'Video generation started in background'
    })

@app.route('/status', methods=['GET'])
def check_status():
    video_path = "path/to/your/outputFile.mp4"
    if os.path.exists(video_path):
        size = os.path.getsize(video_path)
        return jsonify({
            'status': 'ready',
            'video_path': video_path,
            'size_mb': round(size / 1024 / 1024, 2)
        })
    return jsonify({'status': 'processing'})

if __name__ == '__main__':
    app.run(port=5002)