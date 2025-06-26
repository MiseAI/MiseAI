# OpenAI streaming + retry + memory + multi-prompt
import openai
import asyncio
from utils.memory import get_context_messages
from utils.prompts import get_prompt_template

async def stream_ai_response(messages, user_id, org_id, intent):
    history = get_context_messages(user_id, org_id)
    prompt = get_prompt_template(intent)
    full_context = [{"role": "system", "content": prompt}] + history + messages

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=full_context,
            stream=True
        )
        for chunk in response:
            if "choices" in chunk and chunk["choices"][0]["delta"].get("content"):
                yield f"data: {chunk['choices'][0]['delta']['content']}

"
        yield "data: [DONE]

"
    except Exception as e:
        yield f"data: Error: {str(e)}

"
