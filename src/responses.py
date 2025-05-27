import json
import os
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
    if not os.path.exists(prompts_path):
        print(f"WARNING: O arquivo de prompts não foi encontrado no caminho: {prompts_path}")
        raise FileNotFoundError(f"O arquivo de prompts não foi encontrado no caminho: {prompts_path}")

    with open(prompts_path, "r") as file:
        prompts = json.load(file)

    # Format history for the model request
    formatted_history = []
    for msg, answer in historico:
        formatted_history.append({"role": "user", "parts": [msg]})
        formatted_history.append({"role": "model", "parts": [answer]})
    
    formatted_history.append({"role": "user", "parts": [message]})
    
    prompt = prompts.get("prompt1", "Desculpe, não encontrei o prompt.")
    
    # Request the response from the model
    response = model.start_chat(history=formatted_history).send_message(prompt + message)

    if not response.candidates:
        print("WARNING: Nenhuma resposta recebida da API.")
        return "Desculpe, não recebi uma resposta válida da API."
    
    # The appending to history is now handled in app.py
    return response.candidates[0].content.parts[0].text
