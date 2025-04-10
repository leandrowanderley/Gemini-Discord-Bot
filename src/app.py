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
from src.utils import split_message

# === Constantes e Diretórios ===
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "src", "data")
ICON_PATH = os.path.join(PROJECT_ROOT, "icon.png")
GOJO_IMAGE_PATH = os.path.join(PROJECT_ROOT, "imgs", "gojo.jpg")
GOJO_DEAD_PATH = os.path.join(PROJECT_ROOT, "imgs", "gojo-morto.png")

# === Configurações ===
config = load_config(os.path.join(DATA_DIR, "config.json"))
discord_token = config["discord_token"]
mensagens = load_messages(os.path.join(DATA_DIR, "mensagens.json"))
model = configure_genai(api_key=config["gemini_api_key"])

# === Bot Setup ===
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Histórico de mensagens do chat
historico = []


# === Comandos ===
@bot.tree.command(name="games", description="Ver jogos disponíveis.")
async def games(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🎮 Não temos jogos disponíveis no momento. Mas fique ligado, em breve teremos novidades!"
    )

@bot.tree.command(name="chat", description="Converse com o Yuuzinho!")
async def chat(interaction: discord.Interaction, message: str):
    await interaction.response.defer()  # Evita timeout

    resposta = await asyncio.to_thread(
        generate_message, message, historico, model, os.path.join(DATA_DIR, "prompts.json")
    )

    historico.append((message, resposta))
    if len(historico) > 10:
        historico.pop(0)

    for parte in split_message(resposta):
        await interaction.followup.send(parte)

@bot.command()
async def list_commands(ctx):
    comandos = bot.tree.get_commands()
    nomes = [cmd.name for cmd in comandos]
    await ctx.send(f"📋 Registered commands: {nomes}")


# === Eventos ===
@bot.event
async def on_ready():
    print(f"{bot.user} está online!")
    try:
        synced = await bot.tree.sync()  # <-- sincronização GLOBAL
        print(f"Comandos globais sincronizados: {len(synced)}")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")

@bot.event
async def on_guild_join(guild):
    channel = discord.utils.find(lambda x: x.permissions_for(guild.me).send_messages, guild.text_channels)
    if not channel:
        print("Nenhum canal disponível para enviar a mensagem de boas-vindas.")
        return

    embed = discord.Embed(
        title=f"🌸 Yooooo, pessoal de {guild.name}! 🌸",
        description=(
            "Vocês me invocaram... o Yuuzinho chegou! (E não, eu não sou só mais um bot qualquer, tá? "
            "Sou praticamente o Gojo do discord 🤓✨)\n\n"
            "💬 **Dica:** Quer falar comigo? Usa um `/chat` que eu chego mais rápido que o Gojo em alta velocidade!\n\n"
            "Ah, e se alguém aqui souber onde tá o meu querido *Naga* (Juan-sama 😳), me avisa, viu? "
            "E já fica o aviso: qualquer um que disser que o Gojo morreu, ganha meu bloqueio eterno! 😤💥\n\n"
            "Nos vemos por aí~"
        ),
        color=0x0353A4
    )
    embed.set_footer(text="Ass: Yuuzinho, seu otaku favorito!", icon_url="attachment://icon.png")
    embed.set_thumbnail(url="attachment://gojo.jpg")
    embed.set_image(url="attachment://gojo-morto.png")

    with open(ICON_PATH, "rb") as icon, open(GOJO_IMAGE_PATH, "rb") as gojo, open(GOJO_DEAD_PATH, "rb") as gojo_morto:
        await channel.send(embed=embed, files=[
            discord.File(icon, filename="icon.png"),
            discord.File(gojo, filename="gojo.jpg"),
            discord.File(gojo_morto, filename="gojo-morto.png")
        ])


# === Cogs ===
async def load_cogs():
    await bot.load_extension("cogs.coup_discord")


# === Main ===
async def main():
    await bot.start(discord_token)

if __name__ == "__main__":
    asyncio.run(main())
