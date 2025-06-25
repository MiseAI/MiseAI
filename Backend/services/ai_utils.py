
import time
import openai
from openai.error import OpenAIError

def retry_openai_call(create_func, max_retries=3, backoff=2):
    for attempt in range(max_retries):
        try:
            return create_func()
        except OpenAIError as e:
            if attempt < max_retries - 1:
                time.sleep(backoff * (2 ** attempt))
            else:
                raise e


import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_ai_response(messages: list[dict]) -> str:
    response = retry_openai_call(lambda: openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()