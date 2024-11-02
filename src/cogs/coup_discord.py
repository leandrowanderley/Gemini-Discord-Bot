from discord.ext import commands

from games.coup.coup import Coup


class CoupDiscord(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.coup_game = None
        print("CoupDiscord foi inicializado.")

    # Comandos de help do jogo Coup
    @commands.command()
    async def coup_help(self, ctx):
        await ctx.send(
                    "**Coup - Jogo de Cartas**\n\n"
                    "**Comandos disponíveis:**\n\n"
                    "- `/coup_help`  ➜ Mostra esta mensagem de ajuda.\n"
                    "- `/coup_open_game`  ➜ Criar partida.\n"
                    "- `/coup_join`  ➜ Entra na partida.\n"
                    "- `/coup_start`  ➜ Inicia a partida.\n"
                    "- `/coup_status`  ➜ Mostra o status atual da partida.\n"
                    "- `/coup_action_list`  ➜ Exibe a lista de ações disponíveis.\n"
                    "- `/coup_jogadores`  ➜ Mostra os jogadores que estão na partida.\n"
                    "- `/coup_pass`  ➜ Quando todos os jogadores digitarem este comando, significa que ninguém duvida, e a ação será realizada.\n"
                    "- `/coup_duvidar`  ➜ Usado por um jogador para duvidar da ação de outro jogador.\n\n"
                    )

    @commands.command()
    async def coup_action_list(self, ctx):
        await ctx.send(
                    "**Ações disponíveis:**\n\n"
                    "- `/coup_basica`  ➜ Ação básica - Ganhe 1 moeda.\n"
                    "- `/coup_ajudaExterna`  ➜ Ajudar Externa - Ganhe 3 moedas.\n"
                    "- `/coup_coup`  ➜ Golpe de Estado - Pague 7 moedas para eliminar um jogador.\n"
                    "- `/coup_duque`  ➜ Duque - Ganhe 3 moedas.\n"
                    "- `/coup_capitao <nome jogador>`  ➜ Capitão - Roube 2 moedas de outro jogador.\n"
                    "- `/coup_assassino <nome jogador>`  ➜ Assassino - Pague 3 moedas para eliminar um jogador.\n"
                    "- `/coup_embaixador`  ➜ Embaixador - Pegue duas cartas do topo do baralho e escolha duas para devolver ao fundo do baralho.\n"
                    "- `/coup_condessa`  ➜ Condessa - Protege contra o Assassino.\n\n"
                    )

    # Comandos Básicos do Jogo Coup
    @commands.command()
    async def coup_open_game(self, ctx):
        try:
            self.coup_game = Coup("base")
            await ctx.send("Partida de Coup aberta! Use `/coup_join` para entrar na partida.")
            print(f"Partida aberta. Instância de coup_game: {self.coup_game}")
        except Exception as e:
            print(f"ERROS: Erro ao abrir o jogo: {e}")
    
    @commands.command()
    async def coup_join(self, ctx):
        if self.coup_game is None:
            await ctx.send("Nenhuma partida aberta! Use `/coup_open_game` para iniciar uma.")
            return

        print(f"Adicionando jogador: {ctx.author.name}")
        try:
            name = ctx.author.name
            self.coup_game.add_player(name)
            await ctx.send("Jogador(a) adicionado(a) à partida de Coup!")
        except Exception as e:
            print(f"ERROS: Erro ao adicionar jogador de nome {name}: {e}")
            await ctx.send(f"Erro ao adicionar jogador: {name}")
            
    


    @commands.command()
    async def coup_start(self, ctx):
        if self.coup_game is None:
            await ctx.send("Nenhuma partida aberta! Use `/coup_open_game` para iniciar uma.")
            return

        await ctx.send("Partida de Coup iniciada!")
        
        if self.coup_game.players:  # Verifica se a lista de jogadores não está vazia
            players = "Jogadores na partida: " + ", ".join(player.name for player in self.coup_game.players)
            await ctx.send(players)  # Envia a lista de jogadores como mensagem
        else:
            await ctx.send("Nenhum jogador na partida!")
        
        self.coup_game.start_game()
    



async def setup(bot):
    print("Adicionando o cog CoupDiscord...")
    await bot.add_cog(CoupDiscord(bot))

# Esta parte deve ser no final do arquivo
if __name__ == "__main__":
    print("Este módulo não deve ser executado diretamente.")
