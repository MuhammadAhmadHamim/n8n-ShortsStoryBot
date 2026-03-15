<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=shark&color=0:050505,40:1a0010,100:050505&height=220&section=header&text=n8n-ShortsStoryBot&fontSize=36&fontColor=e0e0e0&fontAlignY=45&desc=Zero%20manual%20work.%20Runs%20every%20night.%20Costs%20nothing.&descAlignY=67&descColor=a0a0a0&animation=fadeIn&fontFamily=Georgia" alt="banner"/>

<br/>

![Built In](https://img.shields.io/badge/Built%20In-12%20Hours-e0e0e0?style=for-the-badge&logoColor=black)
![Cost](https://img.shields.io/badge/Monthly%20Cost-%240-1a0010?style=for-the-badge&logoColor=e0e0e0)
![Stack](https://img.shields.io/badge/Stack-n8n%20%2B%20Python%20%2B%20FFmpeg-e0e0e0?style=for-the-badge&logoColor=black)
![Platform](https://img.shields.io/badge/YouTube%20Shorts-Live-2d0018?style=for-the-badge&logo=youtube&logoColor=e0e0e0)
![Status](https://img.shields.io/badge/Status-Shipping%20Daily-050505?style=for-the-badge&logoColor=e0e0e0)

<br/><br/>

> *"The best automation is the one running while you sleep."*

<br/>

</div>

---

## ◈ What Happens Every Night

```
  9:00 PM  ──▶  AI writes a unique storytelling script
  9:01 PM  ──▶  Edge TTS converts it to natural voice
  9:02 PM  ──▶  Pexels fetches relevant stock footage
  9:08 PM  ──▶  FFmpeg builds a complete 9:16 vertical video
  9:10 PM  ──▶  YouTube API uploads — title, tags, description
  9:11 PM  ──▶  Google Sheets logs the URL and date

                You did nothing. It shipped anyway.
```

---

## ◈ The Build Story

**1 PM to 1:30 AM. Ramadan 2026. Islamabad, Pakistan.**
One student. Zero prior experience in n8n, Python servers, or API integration.
Built from scratch. Shipped the same day.

```
✕  4 TTS tools failed before Edge TTS worked
✕  ShortGPT hit 7 missing module errors — abandoned
     └─▶  built a custom video server from scratch instead
✕  YouTube OAuth token kept expiring — debugged cold
✕  n8n timed out on long video generation
     └─▶  solved with async threading
✕  Hit YouTube daily upload limit during testing
     └─▶  paced requests, kept going
```

Every error above is a thing that was figured out in real time with no roadmap.
Full story here → [LinkedIn Post](https://www.linkedin.com/posts/muhammad-ahmad-hamim-676422350_automation-python-buildinpublic-activity-7436513940110516224-SY-E?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFegozoBjvf84TqOA54tISDeSR84nn_MTXs)

---

## ◈ How It's Wired

```
n8n  (localhost:5678)
 │
 ├─ ⏰  Schedule Trigger         fires at 9 PM daily
 ├─ 🤖  OpenRouter               Gemini 2.0 Flash writes the script
 ├─ 🔍  Code Parser              pulls title, description, tags
 ├─ 🔊  tts_server.py  :5001     script  →  MP3
 ├─ 🎬  video_server.py :5002    audio + footage  →  MP4
 ├─ ⏳   Wait Node  (8 min)       FFmpeg needs time
 ├─ 📤  youtube_server.py :5003  MP4  →  YouTube
 └─ 📊  Google Sheets            logs URL + upload date
```

---

## ◈ Full Stack — $0/month

<div align="center">

| Tool | What It Does | Cost |
|:---:|:---|:---:|
| **n8n** | Orchestrates the entire workflow | Free forever |
| **Gemini 2.0 Flash** | Writes the story script via OpenRouter | Free tier |
| **Microsoft Edge TTS** | Narrates the script naturally | Free forever |
| **FFmpeg** | Builds the final vertical video | Free forever |
| **Pexels API** | Supplies the stock footage | Free tier |
| **YouTube Data API v3** | Handles the upload | Free |
| **Google Sheets API** | Logs every upload | Free |
| **Flask** | Powers the three local servers | Free forever |

</div>

---

## ◈ File Structure

```
n8n-ShortsStoryBot/
│
├── tts_server.py                            ←  text  →  MP3  via Edge TTS
├── video_server.py                          ←  audio + footage  →  MP4  via FFmpeg
├── youtube_server.py                        ←  MP4  →  YouTube  via Google API
├── StartAutomation.bat                      ←  one double-click starts everything
├── requirements.txt                         ←  to install all dependencies in one command
├── YT_Shorts_Daily_Automation.json          ←  pre-built n8n workflow — import directly     
└── README.md
```

---

## ◈ Get It Running

**1 — Clone**
```bash
git clone https://github.com/MuhammadAhmadHamim/n8n-ShortsStoryBot
pip install -r requirements.txt
```

**2 — Drop in your keys & paths**
```python
#YT_Shorts_Daily_Automation.json
"value": "YOUR_GOOGLE_SHEET_ID"
"id": "your google sheets id"
"instanceId": "YOUR_INSTANCE_ID"
"value": "path/to/your/file.mp4"
"value": "Bearer YOUR OPENROUTER_KEY"

# tts_server.py
output_file = 'path/to/your/outputFile.mp3'
os.makedirs('path/to/folder/just before/outputFile/', exist_ok=True)

# video_server.py
PEXELS_API_KEY = "your-key"
audio_path = "path/to/your/outputFile.mp3"
output_path = "path/to/your/outputFile.mp4"
clips_dir = "path/to/folder/to save/clips"
os.makedirs("path/to/folder/just before/outputFile", exist_ok=True)
video_path = "path/to/your/outputFile.mp4"

# youtube_server.py
CREDENTIALS_FILE = "path/to/credentials.json"
TOKEN_FILE       = "path/to/token.pickle"
video_path = data.get('video_path', 'path/to/your/outputFile.mp4')

# startAutomation.bat
start cmd /k "cd /d path/to/your/ && python tts_server.py"
start cmd /k "cd /d path/to/your/ && python video_server.py"
start cmd /k "cd /d path/to/your/ && python youtube_server.py"
```

**3 — Google OAuth**
```
console.cloud.google.com
  → New Project
  → Enable: YouTube Data API v3 + Sheets API + Drive API
  → OAuth 2.0 credentials (Desktop App)
  → Download credentials.json → drop in project root
  → Add Gmail as test user in consent screen
```

**4 — Import the n8n workflow**
```bash
1. Run `n8n` in terminal
2. Open http://localhost:5678
3. Click the menu (top left) → Import from File
4. Select `YT_Shorts_Daily_Automation.json` from the project folder
5. Workflow loads with all nodes pre-configured
6. Set your OpenRouter and Google Sheets credentials inside n8n
7. Set Schedule Trigger to your preferred time
8. Click Activate
```

**5 — Launch**
```
StartAutomation.bat  ←  double click
All three remaining servers start. n8n does the rest.
```

**Requirements:** Python 3.10+ · Node.js v20+ · FFmpeg on PATH · n8n global install

---

## ◈ The Niche

```
Content type  →  Betrayal. Redemption. Revenge. Twists. Life lessons.
Variety       →  AI rotates story types — infinite, never repeats
RPM           →  $12 – $16
Uploads       →  1 per day, fully hands-off
```
---

## ◈ Skills This Project Demonstrates

<div align="center">

![](https://img.shields.io/badge/Python-Flask%20Server%20Design-1a0010?style=flat-square&logo=python&logoColor=e0e0e0)
![](https://img.shields.io/badge/Python-Async%20Threading-e0e0e0?style=flat-square&logo=python&logoColor=black)
![](https://img.shields.io/badge/n8n-Workflow%20Automation-1a0010?style=flat-square&logo=node.js&logoColor=e0e0e0)
![](https://img.shields.io/badge/FFmpeg-Video%20Processing-e0e0e0?style=flat-square&logo=ffmpeg&logoColor=black)
![](https://img.shields.io/badge/REST%20APIs-Multi%20Service%20Integration-1a0010?style=flat-square&logo=fastapi&logoColor=e0e0e0)
![](https://img.shields.io/badge/YouTube%20API-OAuth%202.0%20%26%20Upload-e0e0e0?style=flat-square&logo=youtube&logoColor=black)
![](https://img.shields.io/badge/Google%20Sheets%20API-Automated%20Logging-1a0010?style=flat-square&logo=googlesheets&logoColor=e0e0e0)
![](https://img.shields.io/badge/Edge%20TTS-Voice%20Synthesis-e0e0e0?style=flat-square&logo=microsoft&logoColor=black)
![](https://img.shields.io/badge/Pexels%20API-Dynamic%20Media%20Fetching-1a0010?style=flat-square&logo=pexels&logoColor=e0e0e0)
![](https://img.shields.io/badge/Prompt%20Engineering-AI%20Script%20Generation-e0e0e0?style=flat-square&logo=openai&logoColor=black)
![](https://img.shields.io/badge/OAuth%202.0-Token%20Management-1a0010?style=flat-square&logo=auth0&logoColor=e0e0e0)
![](https://img.shields.io/badge/System%20Design-Multi%20Server%20Pipeline-e0e0e0?style=flat-square&logo=buffer&logoColor=black)

</div>

---

## ◈ Contribute

Open a PR — especially for:
- Mac / Linux startup script
- Railway / cloud deployment guide
- Video transition improvements
- Auto thumbnail generation

**License: MIT** — use it, fork it, ship it.

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=shark&color=0:1a0010,40:050505,100:1a0010&height=100&section=footer&text=Built%20in%20one%20night.%20Running%20every%20night.&fontSize=16&fontColor=a0a0a0&fontAlignY=55&animation=fadeIn" alt="footer"/>

</div>
