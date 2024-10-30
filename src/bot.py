import json
import discord
import random
from discord.ext import commands
import google.generativeai as genai
from gemini import generate_message

def split_message(message):
    return [message[i:i + 2000] for i in range(0, len(message), 2000)]

def gerar_resposta(message):    
    try:
        resposta = generate_message(message, historico)
        historico.append((message, resposta))
        if len(historico) > 10:
            historico.pop(0)
        print("INFO: Resposta gerada e histórico atualizado.")
        return resposta
    except Exception as e:
        print(f"ERROR: Falha na API GeminiAPI - {e}")
        return "Desculpe, ocorreu um erro ao gerar a resposta."


with open(r"D:\programacao\Gemini-Discord-Bot\src\config.json", "r") as file:
    config = json.load(file)

discord_token = config["discord_token"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Lista para armazenar o histórico de mensagens e respostas
historico = []

@bot.command()
async def chat(ctx, *, message: str):
    gemini_answer = gerar_resposta(message)
    
    messages = split_message(gemini_answer)
    for msg in messages:
        await ctx.send(msg)
    print(f"INFO: Comando /chat acionado por {ctx.author.name}.")

with open("D:\\programacao\\Gemini-Discord-Bot\\src\\mensagens.json", "r", encoding="utf-8") as file:
    mensagens_data = json.load(file)
    mensagens = mensagens_data["mensagens"]

print("INFO: Mensagens da DM carregadas com sucesso.")

@bot.event
async def on_voice_state_update(member, before, after):

    numero_random = random.randint(1, 100)
    if numero_random > 5:
        print(f"INFO: Detecção de entrada ignorada para {member.name} || Número: {numero_random}")
        return

    if before.channel is None and after.channel is not None:

        mensagem_escolhida = random.choice(mensagens).replace("{nome}", member.name)
        
        try:
            await member.send(mensagem_escolhida)
            print(f"INFO: Mensagem enviada para {member.name} ao entrar no canal de voz.")
        except discord.Forbidden:
            print(f"WARNING: Falha ao enviar mensagem direta para {member.name} - acesso negado.")




bot.run(discord_token)
