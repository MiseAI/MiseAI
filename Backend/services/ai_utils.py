import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_ai_response(messages: list[dict]) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()