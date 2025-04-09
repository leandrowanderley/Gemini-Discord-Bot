# Imports necessários para o funcionamento do bot
import random
import discord
from discord.ext import commands
from discord import app_commands

# Imports locais
from src.config import load_config, load_messages
from src.responses import configure_genai, generate_message
from src.utils import split_message
import os

# Base path do projeto
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "src", "data")

# Carregar configurações
config = load_config(os.path.join(DATA_DIR, "config.json"))
discord_token = config["discord_token"]
mensagens = load_messages(os.path.join(DATA_DIR, "mensagens.json"))
historico = []

# Configurar API do Gemini
model = configure_genai(api_key=config["gemini_api_key"])

# Configurar bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Função para carregar cogs
async def load_cogs():
    await bot.load_extension("cogs.coup_discord")  # Carregar o novo cog

# Evento quando o bot estiver pronto / Conexão com o Discord
@bot.event
async def on_ready():
    print(f"{bot.user} está online e pronto para uso!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# Comando para interagir com a IA
@bot.command()
async def chat(ctx, *, message: str):
    print(f"INFO: Comando /chat acionado por {ctx.author.name}.")
    gemini_answer = generate_message(message, historico, model, os.path.join(DATA_DIR, "prompts.json"))
    historico.append((message, gemini_answer))

    if len(historico) > 10:
        historico.pop(0)

    for msg in split_message(gemini_answer):
        await ctx.send(msg)

    print(f"INFO: Interação /chat acionado por {ctx.author.name} finalizada.")

@bot.command()
async def games(ctx):
    await ctx.send("Não temos jogos disponíveis no momento. Mas fique ligado, em breve teremos novidades! 🎮✨")
    # await ctx.send("Jogos disponíveis: Coup (/coup_help)")

# Evento quando um usuário entra em um canal de voz / Manda uma DM ao usuário de forma aleatória
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None and random.randint(1, 100) <= 5:
        mensagem_escolhida = random.choice(mensagens).replace("{nome}", member.name)
        try:
            await member.send(mensagem_escolhida)
            print(f"INFO: Mensagem enviada para {member.name} ao entrar no canal de voz.")
        except discord.Forbidden:
            print(f"WARNING: Falha ao enviar mensagem direta para {member.name} - acesso negado.")

# Evento quando bot entrar em servidor / Mensagem a entrar em servidor
@bot.event
async def on_guild_join(guild):
    channel = discord.utils.find(lambda x: x.permissions_for(guild.me).send_messages, guild.text_channels)
    if channel:
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

        with open("/Users/leandrowanderley/Documents/programacao/own-projects/Gemini-Discord-Bot/icon.png", "rb") as icon_file, \
             open("/Users/leandrowanderley/Documents/programacao/own-projects/Gemini-Discord-Bot/imgs/gojo.jpg", "rb") as gojo_file, \
             open("/Users/leandrowanderley/Documents/programacao/own-projects/Gemini-Discord-Bot/imgs/gojo-morto.png", "rb") as gojo_morto_file:

            await channel.send(embed=embed, files=[
                discord.File(icon_file, filename="icon.png"),
                discord.File(gojo_file, filename="gojo.jpg"),
                discord.File(gojo_morto_file, filename="gojo-morto.png")
            ])
    else:
        print("Nenhum canal disponível para enviar a mensagem de boas-vindas.")

# Carregar cogs e iniciar o bot
async def main():
    # await load_cogs()
    await bot.start(discord_token)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
