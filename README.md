# Gemini Audio Engineer (Backend & Web Interface) 🧠🎛️

This repository contains the intelligence layer for the **Gemini Audio Engineer** ecosystem. It provides a FastAPI server that acts as the bridge between your Digital Audio Workstation (via the AUv3 plugin) and Google's Gemini AI.

## 🌟 Overview

When the AUv3 plugin captures audio from your DAW, it sends it here. This backend handles:
1. **Audio Processing:** Slicing, normalizing, and generating detailed spectrograms of the captured audio.
2. **AI Inference:** Packaging the audio context and spectrograms and sending them to Gemini with specialized Mixing, Producing, and Executing prompts.
3. **DSP Parsing:** Converting the AI's natural language mixing advice into a strict, structured JSON payload.
4. **Delivery:** Serving that JSON back to the AUv3 plugin so it can instantly apply the EQ, Compression, Saturation, De-essing, and Reverb parameters to your track.

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- A valid Google Gemini API key

### Installation
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Set up your virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Set your environment variables in `.env`:
   ```bash
   GEMINI_API_KEY=your_api_key_here
   ```

### Running the Server
Run the FastAPI application using `uvicorn`:
```bash
source .venv/bin/activate
uvicorn app:app --reload --port 8000
```
The AUv3 plugin automatically polls `http://localhost:8000/health` to confirm the connection.

## 🧩 Modifying the AI Prompts
If you want to train the AI to focus on specific genres or add new DSP tools, check out `backend/prompts.py` and `backend/dsp_parser.py`. The AI has been heavily tuned to provide conservative, realistic mixing moves rather than destructive changes.
