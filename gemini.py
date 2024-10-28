import json
import google.generativeai as genai

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
def generate_message(message):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(message)
    
    # Extrair o texto da resposta
    return response.candidates[0].content.parts[0].text