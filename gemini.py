import json
import google.generativeai as genai
from google.generativeai.types import Content

with open("config.json", "r") as file:
    config = json.load(file)

genai.configure(api_key=config["gemini_api_key"])

# Configurações do modelo
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Criação do modelo
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Função para gerar a mensagem
def generate_message(message, historico):
    formatted_history = []
    
    for user_msg, bot_msg in historico:
        formatted_history.append(Content(role="user", content=user_msg))
        formatted_history.append(Content(role="model", content=bot_msg))

    formatted_history.append(Content(role="user", content=message))
    
    chat_session = model.start_chat(history=formatted_history)
    response = chat_session.send_message(message)
    print(response) 
    # Extrair o texto da resposta
    if hasattr(response, 'candidates') and response.candidates:
        return response.candidates[0].content.parts[0].text
    else:
        return "Desculpe, não recebi uma resposta válida da API."


generate_message("Apartir de agora você é vascaino", [])