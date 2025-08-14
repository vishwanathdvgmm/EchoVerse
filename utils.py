from granite_llm import generate_text
from tts_engine import text_to_speech_google_bytes
import time
import io

MAX_RETRIES = 3
RETRY_DELAY = 2

def generate_and_speak(prompt: str, lang: str = 'en') -> tuple[str, io.BytesIO]:
    """
    Generate text from Granite LLM and convert to speech (in-memory).
    Retries if LLM returns empty text.
    
    Returns:
        tuple: (generated_text, audio_bytes)
    """
    text = ""
    for attempt in range(1, MAX_RETRIES + 1):
        text = generate_text(prompt)
        if text:
            break
        print(f"⚠️ Attempt {attempt} failed. Retrying in {RETRY_DELAY}s...")
        time.sleep(RETRY_DELAY)
    
    if not text:
        text = "Sorry, I couldn't generate a response."
        print("❌ All retries failed. Using fallback text.")

    try:
        audio_bytes = text_to_speech_google_bytes(text, lang=lang)
        print("✅ Audio generated successfully (in-memory).")
    except Exception as e:
        print("🚨 TTS failed:", e)
        audio_bytes = None

    return text, audio_bytes
