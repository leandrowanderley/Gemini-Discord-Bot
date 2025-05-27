# Código Atual (Problemático)	                Lógica a ser implementada (Correta)
# historico = [] (global)	                    historicos_por_servidor = {} (global)
# Usa a mesma historico sempre.	                1. Pega o ID do servidor: guild_id = interaction.guild.id
#                                               2. Pega o histórico certo: historico_especifico = historicos_por_servidor.get(guild_id, [])
# generate_message(..., historico, ...)	        generate_message(..., historico_especifico, ...)
# historico.append(...)	                        historico_especifico.append(...)
# Nada mais a fazer.	                        3. Salva a lista atualizada:
#                                               historicos_por_servidor[guild_id] = historico_especifico




# === Imports Padrão ===
import os
import random
import asyncio

# === Imports de Terceiros ===
import discord
from discord import app_commands
from discord.ext import commands

# === Imports Locais ===
from src.config import load_config, load_messages
from src.responses import configure_genai, generate_message
from src.utils.split_message import split_message
from src.utils.logger import log

# === Constantes e Diretórios ===
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "src", "data")
ICON_PATH = os.path.join(PROJECT_ROOT, "icon.png")
GOJO_IMAGE_PATH = os.path.join(PROJECT_ROOT, "imgs", "gojo.jpg")
GOJO_DEAD_PATH = os.path.join(PROJECT_ROOT, "imgs", "gojo-morto.png")

# === Configurações ===
log("Carregando configurações...", "info")
config = load_config(os.path.join(DATA_DIR, "config.json"))
discord_token = config["discord_token"]
log("Configurações carregadas com sucesso ✅", "sucesso")

log("Carregando mensagens...", "info")
mensagens = load_messages(os.path.join(DATA_DIR, "mensagens.json"))
log(f"{len(mensagens)} mensagens carregadas com sucesso 📨", "sucesso")

log("Configurando modelo Gemini...", "info")
model = configure_genai(api_key=config["gemini_api_key"])
log("Modelo Gemini configurado com sucesso 🤖", "sucesso")


# === Bot Setup ===
log("Inicializando bot com prefixo '/'...", "info")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
log("Bot inicializado com intents configuradas 🚀", "sucesso")


bot = commands.Bot(command_prefix='/', intents=intents)

# Histórico de mensagens do chat
historico = {}


# === Comandos ===
@bot.tree.command(name="games", description="Ver jogos disponíveis.")
async def games(interaction: discord.Interaction):
    log(f"Comando '/games' invocado por {interaction.user}", "info")
    await interaction.response.send_message(
        "🎮 Não temos jogos disponíveis no momento. Mas fique ligado, em breve teremos novidades!"
    )

@bot.tree.command(name="chat", description="Converse com o Yuuzinho!")
async def chat(interaction: discord.Interaction, message: str):
    log(f"Comando '/chat' chamado por {interaction.user}: '{message}'", "info")
    await interaction.response.defer()
    
    guild_id = interaction.guild.id
    
    historico_especifico = historico.get(guild_id, [])

    resposta = await asyncio.to_thread(
        generate_message, message, historico_especifico, model, os.path.join(DATA_DIR, "prompts.json")
    )

    log("Resposta gerada pelo modelo, enviando para o usuário...", "info")

    historico_especifico.append((message, resposta))
    if len(historico_especifico) > 10:
        log("Histórico ultrapassou 10 entradas, removendo a mais antiga", "aviso")
        historico_especifico.pop(0)
    
    historico[guild_id] = historico_especifico

    for parte in split_message(resposta):
        await interaction.followup.send(parte)

    log("Mensagem enviada com sucesso 📨", "sucesso")

@bot.command()
async def list_commands(ctx):
    log(f"Comando '!list_commands' executado por {ctx.author}", "info")
    comandos = bot.tree.get_commands()
    nomes = [cmd.name for cmd in comandos]
    await ctx.send(f"📋 Registered commands: {nomes}")
    log("Lista de comandos enviada com sucesso 📤", "sucesso")


# === Eventos ===
@bot.event
async def on_ready():
    log(f"{bot.user} está online!", "sucesso")
    try:
        synced = await bot.tree.sync()
        log(f"Comandos globais sincronizados: {len(synced)}", "sucesso")
    except Exception as e:
        log(f"Erro ao sincronizar comandos: {e}", "erro")

@bot.event
async def on_guild_join(guild):
    log(f"Entrou em um novo servidor: {guild.name} ({guild.id})", "info")
    historico[guild.id] = []
    channel = discord.utils.find(lambda x: x.permissions_for(guild.me).send_messages, guild.text_channels)
    if not channel:
        log("Nenhum canal disponível para enviar a mensagem de boas-vindas.", "aviso")
        return
    log(f"Canal detectado: {channel.name} - Enviando mensagem de boas-vindas...", "info")


# === Cogs ===
async def load_cogs():
    try:
        await bot.load_extension("cogs.coup_discord")
        log("Cog 'coup_discord' carregado com sucesso 🧩", "sucesso")
    except Exception as e:
        log(f"Erro ao carregar cog 'coup_discord': {e}", "erro")


# === Main ===
async def main():
    log("Iniciando o bot com token do Discord...", "info")
    # await load_cogs()
    await bot.start(discord_token)

if __name__ == "__main__":
    asyncio.run(main())
