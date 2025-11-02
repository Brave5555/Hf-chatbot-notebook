# chatbot.py
from typing import List, Dict
from config import get_hf_client

SYSTEM_PROMPT = "You are a concise, helpful assistant."

# create client once
client = get_hf_client()

def chat_once(user_message: str) -> str:
    
    resp = client.chat_completion(
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        max_tokens=256,   # 256 - ensures answers are not too long
        temperature=0.7,  # medium setting
        top_p=0.95,
    )
    
    reply = resp.choices[0].message.get("content", "")
    return reply


class ChatSession:
    # in-memory chat session that keeps conversation history
    def __init__(self, system_prompt: str = SYSTEM_PROMPT):
        self.client = client
        self.history: List[Dict[str, str]] = [
            {"role": "system", "content": system_prompt}
        ]

    def send(self, user_message: str) -> str:
        self.history.append({"role": "user", "content": user_message})
        resp = self.client.chat_completion(
            messages=self.history,
            max_tokens=256,
            temperature=0.7,
            top_p=0.95,
        )
        reply = resp.choices[0].message.get("content", "")
        self.history.append({"role": "assistant", "content": reply})
        return reply
