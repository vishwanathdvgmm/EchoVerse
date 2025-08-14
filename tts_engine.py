import requests
import io
import config

MAX_CHARS = 200

def split_text(text: str, max_len: int = MAX_CHARS):
    words = text.split()
    chunks = []
    current_chunk = ""
    for word in words:
        if len(current_chunk) + len(word) + 1 > max_len:
            chunks.append(current_chunk.strip())
            current_chunk = word
        else:
            current_chunk += " " + word
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def text_to_speech_google_bytes(text: str, lang='en') -> io.BytesIO:
    """
    Generate Google TTS audio as in-memory MP3 bytes.
    Returns a BytesIO object for Streamlit playback/download.
    """
    if getattr(config, "DEFAULT_TONE", None):
        text = f"[{config.DEFAULT_TONE} tone] {text}"

    chunks = split_text(text, MAX_CHARS)
    combined_audio = io.BytesIO()

    for i, chunk in enumerate(chunks):
        tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={chunk}&tl={lang}&client=tw-ob"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
        response = requests.get(tts_url, headers=headers)
        if response.status_code == 200:
            combined_audio.write(response.content)
        else:
            raise RuntimeError(f"TTS request failed for chunk {i+1}: {response.status_code}")

    combined_audio.seek(0)
    return combined_audio
