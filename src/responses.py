
import json
import google.generativeai as genai

def configure_genai(api_key, model_name="gemini-1.5-flash"):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(
        model_name=model_name,
        generation_config={
            "temperature": 0.8,
            "top_p": 0.9,
            "top_k": 50,
            "max_output_tokens": 4000,
            "response_mime_type": "text/plain",
        }
    )

def generate_message(message, historico, model, prompts_path):
    with open(prompts_path, "r") as file:
        prompts = json.load(file)

    formatted_history = [{"role": "user", "parts": [msg]} if i % 2 == 0 else {"role": "model", "parts": [msg]}
                         for i, (msg, _) in enumerate(historico)]

    prompt = prompts["gojo"] if any(keyword in message.lower() for keyword in ["ele", "morreu", "gojo"]) else prompts["default"]
    response = model.start_chat(history=formatted_history).send_message(prompt + message)

    return response.candidates[0].content.parts[0].text if response.candidates else "Desculpe, não recebi uma resposta válida da API."
