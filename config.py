# config.py
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv("HF Chat.env")  

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"

def get_hf_client() -> InferenceClient:
    token = os.getenv("HF_TOKEN")
    if not token:
        raise RuntimeError("HF_TOKEN not found in .env")
    return InferenceClient(model=MODEL_ID, token=token)
