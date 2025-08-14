from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import config

try:
    tokenizer = AutoTokenizer.from_pretrained(config.LLM_MODEL, use_auth_token=config.HF_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(config.LLM_MODEL, use_auth_token=config.HF_TOKEN)
    llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
    print("[INFO] LLM pipeline loaded successfully.")
except Exception as e:
    print("🚨 Failed to load LLM pipeline:", e)
    llm_pipeline = None

def generate_text(prompt: str, max_length: int = 500, temperature: float = 0.7) -> str:
    """
    Generate text from the Granite LLM.
    """
    if not llm_pipeline:
        print("🚨 LLM pipeline not initialized.")
        return ""
    
    try:
        output = llm_pipeline(
            prompt,
            max_length=max_length,
            temperature=temperature,
            do_sample=True,
            truncation=True
        )
        text = output[0].get("generated_text", "").strip()
        if not text:
            print("⚠️ LLM returned empty string.")
        else:
            print("[LLM OUTPUT]:", text)
        return text
    except Exception as e:
        print("🚨 LLM generation failed:", e)
        return ""
