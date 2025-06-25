
import os
import openai
from services.query_intent import simple_fallback

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(prompt: str) -> str:
    if openai.api_key:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a restaurant business assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"OpenAI error: {str(e)}"
    else:
        return simple_fallback(prompt)
