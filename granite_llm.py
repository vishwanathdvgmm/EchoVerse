from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import config
import torch

device = torch.device("cpu")

try:
    tokenizer = AutoTokenizer.from_pretrained(config.LLM_MODEL, token=config.HF_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(config.LLM_MODEL, token=config.HF_TOKEN)
    llm_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1
    )
    print("[INFO] LLM pipeline loaded successfully.")
except Exception as e:
    print("🚨 Failed to load LLM pipeline:", e)
    llm_pipeline = None

def generate_text(prompt: str, max_new_tokens: int = 150, temperature: float = 0.7, top_p: float = 0.9, repetition_penalty: float = 1.2) -> str:
    """
    Generate text from Granite LLM with improved control.
    
    Args:
        prompt (str): The input prompt.
        max_new_tokens (int): Max tokens to generate in this call.
        temperature (float): Controls randomness; 0 = deterministic.
        top_p (float): Nucleus sampling; keeps top tokens summing to top_p probability.
        repetition_penalty (float): >1 discourages repeated text.
    
    Returns:
        str: Generated text.
    """
    if not llm_pipeline:
        print("🚨 LLM pipeline not initialized.")
        return ""

    try:
        output = llm_pipeline(
            prompt,
            max_new_tokens=100,
            temperature=0.6,
            top_p=0.9,
            repetition_penalty=1.2,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
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
