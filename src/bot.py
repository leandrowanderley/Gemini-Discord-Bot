import json
import discord
from discord.ext import commands
import google.generativeai as genai
from gemini import generate_message

with open(r"D:\programacao\Gemini-Discord-Bot\src\config.json", "r") as file:
    config = json.load(file)

discord_token = config["discord_token"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Lista para armazenar o histórico de mensagens e respostas
historico = []

def gerar_resposta(message):
    try:
        resposta = generate_message(message, historico)
        # Atualiza o histórico
        historico.append((message, resposta))
        # Mantém apenas as últimas 10 mensagens e respostas
        if len(historico) > 10:
            historico.pop(0)
        return resposta
    except Exception as e:
        print(f"Erro na API GeminiAPI: {e}")
        return "Desculpe, ocorreu um erro ao gerar a resposta."

@bot.command()
async def chat(ctx, *, message: str):
    gemini_answer = gerar_resposta(message)
    await ctx.send(gemini_answer)

bot.run(discord_token)
