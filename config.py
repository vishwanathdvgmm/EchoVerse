import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
LLM_MODEL = os.getenv("LLM_MODEL")

DEFAULT_TONE = os.getenv("DEFAULT_TONE", "Neutral")
DEFAULT_VOICE = os.getenv("DEFAULT_VOICE", "Female A (clear)")
