import json
import google.generativeai as genai

with open("config.json", "r") as file:
    config = json.load(file)

gemini_token = config["gemini_api_key"]

genai.configure(api_key=gemini_token)

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
    
    # Adiciona o histórico de mensagens no formato de dicionário certo
    for user_msg, bot_msg in historico:
        formatted_history.append({
            "role": "user",
            "parts": [user_msg]
        })
        formatted_history.append({
            "role": "model",
            "parts": [bot_msg]
        })

    # Adiciona a nova mensagem do usuário
    formatted_history.append({
        "role": "user",
        "parts": [message]
    })
    
    # Inicia uma nova sessão de chat com o histórico formatado
    chat_session = model.start_chat(history=formatted_history)
    response = chat_session.send_message(message)

    # Extrair o texto da resposta
    if hasattr(response, 'candidates') and response.candidates:
        return response.candidates[0].content.parts[0].text
    else:
        return "Desculpe, não recebi uma resposta válida da API."


# historico_inicial = [
#     ("Apartir de agora você é vascaino", "E aí, vascaíno! ⚡️🖤🤍 A partir de agora, a torcida vai ser ainda mais forte! Me contem tudo sobre o Gigante da Colina: qual o seu ídolo, a sua maior conquista, o que te deixa mais feliz como vascaíno?  Estou pronto para vibrar com cada gol, cada vitória e cada momento épico do Vasco! 🏆 Vamos juntos rumo à glória! 👊")
# ]
# x = generate_message("que coisa boa. qual o maior jogador da historia do seu time", historico_inicial)

# print(x)