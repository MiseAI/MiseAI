# Prompt factory
prompt_templates = {
    "general": "You are MiseAI, a helpful kitchen assistant...",
    "menu": "You are helping create and analyze restaurant menus...",
    "forecast": "You are assisting with sales forecasting for foodservice...",
}

def get_prompt_template(intent):
    return prompt_templates.get(intent, prompt_templates["general"])
