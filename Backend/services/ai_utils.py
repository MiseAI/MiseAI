import openai

def get_ai_response(prompt: str) -> str:
    openai.api_key = "sk-..."  # Replace with your key or env var
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
