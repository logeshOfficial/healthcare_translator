import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

language_map = {
    "English": "English",
    "Tamil": "Tamil (India)",
    "Hindi": "Hindi (India)",
    "Japanese": "Japanese",
    "Chinese": "Chinese (Simplified)"
}

def translate_medical_text(text, target_language):
    prompt = f"""
You are a professional medical interpreter.

Tasks:
1. Correct minor speech recognition errors.
2. Preserve medical meaning.
3. Translate into {language_map[target_language]}.
4. Keep language simple and patient-friendly.

Transcript:
{text}
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
        )

        return response.text.strip()
    except Exception as ex:
        return f"Translation failed due to {ex}. Please try again."