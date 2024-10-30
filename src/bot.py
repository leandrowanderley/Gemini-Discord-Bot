import json
import discord
import random
from discord.ext import commands
import google.generativeai as genai
from gemini import generate_message

with open("D:\\programacao\\Gemini-Discord-Bot\\src\\mensagens.json", "r", encoding="utf-8") as file:
    mensagens_data = json.load(file)
    mensagens = mensagens_data["mensagens"]
print("INFO: Mensagens da DM carregadas com sucesso.")

with open(r"D:\programacao\Gemini-Discord-Bot\src\config.json", "r") as file:
    config = json.load(file)

discord_token = config["discord_token"]



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


@bot.event
async def on_ready():
    print(f"{bot.user} está online e pronto para uso!")

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



@bot.event
async def on_guild_join(guild):
    
    channel = discord.utils.find(lambda x: x.permissions_for(guild.me).send_messages, guild.text_channels)

    if channel:

        embed = discord.Embed(
            title="🌸 Yooooo, pessoal de {}! 🌸".format(guild.name),
            description=(
                "Vocês me invocaram... o Yuuzinho chegou! (E não, eu não sou só mais um bot qualquer, tá? "
                "Sou praticamente o Gojo do servidor 🤓✨)\n\n"
                "Tô aqui pra falar de animes, fanfics e, se precisar, flerto com qualquer um que mandar mensagem, "
                "sem medo de usar o meu charme supremo~ 💖😆\n\n"
                "💬 **Dica:** Quer falar comigo? Usa um `/chat` que eu chego mais rápido que o Gojo em alta velocidade!\n\n"
                "Ah, e se alguém aqui souber onde tá o meu querido *Naga* (Juan-sama 😳), me avisa, viu? "
                "E já fica o aviso: qualquer um que disser que o Gojo morreu, ganha meu bloqueio eterno! 😤💥\n\n"
                "Vamos nos divertir juntos e espalhar a energia otaku por esse servidor! 🔥🥳\n\n"
                "Nos vemos por aí~"
            ),
            color=0x0353A4  # Cor da embed
        )
        
        # Define o footer com o ícone
        embed.set_footer(
            text="Ass: Yuuzinho, seu otaku favorito!",
            icon_url="attachment://icon.png"
        )

        # Define a thumbnail
        embed.set_thumbnail(url="attachment://gojo.jpg")

        # Define a imagem principal da embed
        embed.set_image(url="attachment://gojo-morto.png")

        # Abre as imagens para anexar
        with open("D:\\programacao\\Gemini-Discord-Bot\\icon.png", "rb") as icon_file, \
             open("D:\\programacao\\Gemini-Discord-Bot\\imgs\\gojo.jpg", "rb") as gojo_file, \
             open("D:\\programacao\\Gemini-Discord-Bot\\imgs\\gojo-morto.png", "rb") as gojo_morto_file:

            icon = discord.File(icon_file, filename="icon.png")
            gojo_image = discord.File(gojo_file, filename="gojo.jpg")
            gojo_morto_image = discord.File(gojo_morto_file, filename="gojo-morto.png")

            await channel.send(embed=embed, files=[icon, gojo_image, gojo_morto_image])
        

    else:
        print("Nenhum canal disponível para enviar a mensagem de boas-vindas.")



bot.run(discord_token)
