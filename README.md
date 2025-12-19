# 🩺 Healthcare Translation Web App (Generative AI)

## Overview

This project is a **real-time healthcare translation web application** designed to enable clear, multilingual communication between patients and healthcare providers. The app converts spoken input into text, displays a live transcript, translates it into a selected language using **Generative AI**, and provides audio playback of the translated content.

The primary goal of this prototype is **rapid development with quality**, leveraging generative AI tools for both translation and development assistance.

---

## Key Features

* 🎙️ **Voice-to-Text Transcription**

  * Uses browser-based Speech Recognition (Web Speech API)
  * Supports continuous speech input
  * Optimized for medical conversations

* 🌍 **Generative AI Translation**

  * Medical-aware translation using Google Gemini
  * Corrects minor speech recognition errors
  * Preserves clinical meaning while remaining patient-friendly

* 🧾 **Dual Transcript Display**

  * Original transcript
  * Translated transcript in real time

* 🔊 **Text-to-Speech Playback**

  * Audio playback of translated text
  * Language-specific speech synthesis

* 📱 **Mobile-First & Responsive UI**

  * Works on mobile, tablet, and desktop devices

---

## Tech Stack

### Frontend

* **Streamlit**
* **HTML + JavaScript** (via `streamlit.components`)
* **Web Speech API** (Speech Recognition & Text-to-Speech)

### AI / Backend

* **Google Gemini (Generative AI)**

  * Model: `gemini-2.5-flash-lite`
  * Used for translation and medical language refinement

### Deployment

* **Streamlit Community Cloud** (Live prototype)

---

## Application Architecture

```
User Speech
   ↓
Browser Speech Recognition (Web Speech API)
   ↓
Live Transcript (Original Language)
   ↓
Generative AI (Medical Translation & Correction)
   ↓
Translated Transcript
   ↓
Text-to-Speech Playback
```

---

## Generative AI Usage

Generative AI is used in two key areas:

1. **Medical Translation**

   * Translates conversations between selected languages
   * Preserves clinical terminology and intent
   * Simplifies language for patient comprehension

2. **AI-Assisted Development**

   * Used for rapid prototyping
   * Prompt refinement and error handling
   * UX and code structure optimization

### Translation Prompt Strategy

The AI is instructed to:

* Correct minor speech recognition errors
* Preserve medical meaning
* Translate accurately into the target language
* Use patient-friendly language

---

## Supported Languages

* English
* Tamil (India)
* Hindi (India)

Additional languages can be easily added.

---

## Data Privacy & Security Considerations

* ❌ No audio or text data is stored
* ❌ No database or logging
* ✅ All processing is done in memory
* ✅ API keys stored securely using environment variables
* ✅ HTTPS enabled via deployment platform

This ensures basic patient confidentiality suitable for a prototype.

---

## How to Run Locally

### 1. Clone the Repository

```bash
git clone <repository-url>
cd healthcare-translator
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## User Guide

1. Select **Input Language** and **Output Language**
2. Click **Start** and speak into the microphone
3. Stop recording when finished
4. Copy the transcript and paste it into the input field
5. Click **Translate**
6. View translated text
7. Click **Speak Translation** to hear audio output

---

## Recording Requirement

A screen recording was captured during development to demonstrate:

* Application design decisions
* Use of generative AI tools
* Debugging and problem-solving approach
* Rapid prototyping workflow

---

## Limitations & Future Improvements

* Direct streaming transcription into the app without copy-paste
* Medical glossary integration
* Role-based access for providers and patients
* HIPAA-compliant backend for production use

---

## Conclusion

This prototype demonstrates the effective use of **Generative AI**, **speech technologies**, and **rapid development practices** to solve real-world healthcare communication challenges.
