import os
import openai
from fastapi import HTTPException
from tenacity import retry, stop_after_attempt, wait_fixed

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = (
    "You are MiseAI, an AI assistant specialized in restaurant operations. "
    "Provide concise and actionable insights based on user requests."
)

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def call_openai(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )
        return response
    except Exception as e:
        print(f"OpenAI API error: {e}")
        raise

def get_chat_response(user_messages):
    msgs = [{"role": "system", "content": SYSTEM_PROMPT}]
    msgs.extend([{"role": m.role, "content": m.content} for m in user_messages])
    try:
        res = call_openai(msgs)
        return res.choices[0].message.content
    except Exception:
        raise HTTPException(status_code=502, detail="AI service unavailable")
