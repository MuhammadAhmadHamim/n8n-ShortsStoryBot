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
Full story here → [LinkedIn Post](YOUR_LINKEDIN_POST_URL)

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
├── tts_server.py          ←  text  →  MP3  via Edge TTS
├── video_server.py        ←  audio + footage  →  MP4  via FFmpeg
├── youtube_server.py      ←  MP4  →  YouTube  via Google API
├── StartAutomation.bat    ←  one double-click starts everything
├── requirements.txt
└── README.md
```

---

## ◈ Get It Running

**1 — Clone**
```bash
git clone https://github.com/MuhammadAhmadHamim/n8n-ShortsStoryBot
pip install -r requirements.txt
```

**2 — Drop in your keys**
```python
# video_server.py
PEXELS_API_KEY = "your-key"

# youtube_server.py
CREDENTIALS_FILE = "path/to/credentials.json"
TOKEN_FILE       = "path/to/token.pickle"
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

**4 — Build the n8n workflow**
```
run: n8n
open: http://localhost:5678
build the workflow per the architecture above
set schedule trigger → activate
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
