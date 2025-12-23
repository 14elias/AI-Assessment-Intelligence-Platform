# app/core/ai_client.py
import httpx
from typing import List, Dict
from core.config import settings


class OpenRouterClient:
    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

    def __init__(self):
        self.api_key = settings.API_KEY

    async def chat(self, prompt: str) -> Dict:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            # Optional but recommended by OpenRouter
            "HTTP-Referer": "http://localhost",
            "X-Title": "AlignEd-MVP",
        }

        payload = {
            "model": "openai/gpt-3.5-turbo",  # free-tier friendly
            "messages": [
                {
                    "role": "system",
                    "content": "You are an educational assessment expert."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.2,
        }

        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                self.BASE_URL,
                headers=headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()
