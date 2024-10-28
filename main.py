import json
import discord
from discord.ext import commands
from gemini import generate_message

with open("config.json", "r") as file:
    config = json.load(file)

discord_token = config["discord_token"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

def gerar_resposta(message):
    try:
        return generate_message(message)
    except Exception as e:
        print(f"Erro na API GeminiAPI: {e}")
        return "Desculpe, ocorreu um erro ao gerar a resposta."

@bot.command()
async def chat(ctx, *, message: str):
    gemini_answer = gerar_resposta(message)
    await ctx.send(gemini_answer)

bot.run(discord_token)