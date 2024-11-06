import discord
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
                    "- `/coup_choose_card`  ➜ Escolher carta - Escolha uma carta papa perder.\n"
                    "- `/coup_ordem`  ➜ Ordem de jogadores - Ver a ordem de jogadores da partida.\n"
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



    # Comandos para iniciar o Jogo Coup
    @commands.command()
    async def coup_open_game(self, ctx):
        try:
            self.coup_game = Coup("base")
            await ctx.send("Partida de Coup aberta! Use `/coup_join` para entrar na partida.")
            print(f"INFO: Partida aberta. Instância de coup_game: {self.coup_game}")
        except Exception as e:
            print(f"ERROS: Erro ao abrir o jogo: {e}")
    
    @commands.command()
    async def coup_join(self, ctx):
        if self.coup_game is None:
            await ctx.send("Nenhuma partida aberta! Use `/coup_open_game` para iniciar uma.")
            return

        print(f"INFO: Adicionando jogador: {ctx.author.name}")
        try:
            name = ctx.author.name
            user_id = ctx.author.id
            self.coup_game.add_player(name, user_id)
            await ctx.send("Jogador(a) adicionado(a) à partida de Coup!")
        except Exception as e:
            print(f"ERROS: Erro ao adicionar jogador de nome {name}: {e}")
            await ctx.send(f"Erro ao adicionar jogador: {name}")
            
    @commands.command()
    async def coup_start(self, ctx):
        try:
            if self.coup_game is None:
                await ctx.send("Nenhuma partida aberta! Use `/coup_open_game` para iniciar uma.")
                return

            await ctx.send("Partida de Coup iniciada!")
            
            if self.coup_game.players:
                players = "Jogadores na partida: " + ", ".join(player.name for player in self.coup_game.players)
                await ctx.send(players)
            else:
                await ctx.send("Nenhum jogador na partida!")

            print("INFO: Jogadores na partida:")
            for player in self.coup_game.players:
                print(player)

            self.coup_game.start_game()
            print("INFO: Partida iniciada, e cartas distribuídas!")

            self.coup_game.turn = 0
            self.coup_game.cpass = 0
            print("INFO: Turno escolhido! " + self.coup_game.get_current_player().name + " " + str(self.coup_game.turn))

            for player in self.coup_game.players:
                member = await self.bot.fetch_user(player.id)
                print(member)
                await member.send("Seu status é: " + str(player))

            await ctx.send("Cartas distribuídas! Verifique a DM, lá contém suas cartas. A primeira rodada começa com " + self.coup_game.get_current_player().name)
            print("INFO: Status enviado para os players!")

        except Exception as e:
            print(f"ERRO: {e} ao iniciar a partida.")

            await ctx.send("Ocorreu um erro ao iniciar o jogo.")

    @commands.command()
    async def coup_ordem(self, ctx):
        if self.coup_game is None:
            await ctx.send("Nenhuma partida aberta! Use `/coup_open_game` para iniciar uma.")
            return

        players = self.coup_game.get_players()
        await ctx.send("Ordem dos jogadores: " + ", ".join(players))



    # Comandos de ações do jogo Coup
    @commands.command()
    async def coup_pass(self, ctx):
        if self.coup_game is None:
            await ctx.send("Nenhuma partida aberta! Use `/coup_open_game` para iniciar uma.")
            return
        elif self.coup_game.state == "doubt":
            self.coup_game.cpass += 1
            if self.coup_game.cpass == (len(self.coup_game.players) - 1):
                current_player = self.coup_game.get_current_player()
                self.coup_game.cpass = 0
                self.coup_game.state = "waiting"
                await ctx.send(f"Todos passaram! {current_player} irá realizar a ação de {self.coup_game.action}.")
                self.coup_game.action(current_player)
                self.coup_game.next_turn()
            else:
                await ctx.send("Votos para passar: " + str(self.coup_game.cpass) + "/" + str(len(self.coup_game.players) - 1))
        else:
            await ctx.send("Nada para passar!")

    @commands.command()
    async def coup_basica(self, ctx):
        player = self.coup_game.get_current_player()
        if player.name != ctx.author.name:
            await ctx.send(f"Agora é a vez de {player.name}.")
            return
        if self.coup_game is None:
            await ctx.send("Nenhuma partida aberta! Use `/coup_open_game` para iniciar uma.")
            return

        player = self.coup_game.get_current_player()
        self.coup_game.action_basica(player)
        await ctx.send(f"Ação básica realizada por {player.name}! Ganhou 1 moeda.")
        for player in self.coup_game.players:
            member = await self.bot.fetch_user(player.id)
            print(member)
            await member.send("Seu status é: " + str(player))
        self.coup_game.next_turn()

    @commands.command()
    async def coup_coup(self, ctx, *, message: str):
        if self.coup_game is None:
            await ctx.send("Nenhuma partida aberta! Use `/coup_open_game` para iniciar uma.")
            return
        self.coup_game.action = "coup"
        player = self.coup_game.get_current_player()
        target = self.coup_game.get_player(message)
        self.target = target
        self.coup_game.action_coup(player, target)
        await ctx.send(f"Golpe de Estado realizado por {player.name}! Eliminou uma carta de {target.name}.\n {target.name} escolha uma carta para ser eliminada, use o nome dela.")
        await ctx.send(f"{target.name}, use `/coup_choose_card` para escolher a sua carta para ser eliminada, use o nome da carta na sua DM.")
        self.coup_game.state = "doubt"
        
    @commands.command()
    async def coup_choose_card(self, ctx, *, message: str):
        print("INFO: Comando /coup_choose_card acionado.")
        
        if self.coup_game is None:
            await ctx.send("Nenhuma partida aberta! Use `/coup_open_game` para iniciar uma.")
            print("ERRO: Nenhuma partida aberta no momento.")
            return

        elif self.coup_game.state != "doubt":
            await ctx.send("Não há uma ação em que escolher cartas seja necessário agora.")
            print(f"ERRO: Estado atual do jogo é '{self.coup_game.state}', esperado 'doubt'.")
            return

        target = self.coup_game.get_player(ctx.author.name)
        print(f"INFO: Jogador alvo é {target.name} com cartas: {[card.name for card in target.cards]}")
        
        chosen_card = next((card for card in target.cards if card.name.lower() == message.lower()), None)
        
        if not chosen_card:
            await ctx.send("Nome da carta inválido. Por favor, escolha uma carta válida entre as suas.")
            print(f"ERRO: Carta '{message}' não encontrada nas cartas do jogador {target.name}.")
            print("Cartas do jogador:", [card.name for card in target.cards])
            return

        print(f"INFO: {target.name} escolheu a carta {chosen_card.name} para ser eliminada.")
        
        # Elimina a carta escolhida
        info = self.coup_game.action_choose_card(target, chosen_card)
        if not info:
            await ctx.send(info)
            return  
        
        remaining_cards = [card.name for card in target.cards]
        print(f"INFO: Cartas restantes para {target.name} após eliminação: {remaining_cards}")
        
        await ctx.send(f"{target.name} escolheu a carta {chosen_card.name} para ser eliminada.")

        # Verificação do estado do jogo após a ação
        print(f"INFO: Estado atual do jogo após a eliminação da carta: {self.coup_game.state}")
        

        if self.coup_game.action == "coup":
            self.coup_game.state = "waiting"
            self.coup_game.next_turn()

            # Verificação do turno atual
            current_player = self.coup_game.get_current_player()
            await ctx.send(f"Agora é a vez de: {current_player.name if current_player else 'Nenhum jogador'}")
            
            self.target = ""
            self.coup_game.action == ""

        for player in self.coup_game.players:
            member = await self.bot.fetch_user(player.id)
            print(member)
            await member.send("Seu status é: " + str(player))

    @commands.command()
    async def coup_ajudaExterna(self, ctx):
        player = self.coup_game.get_current_player()
        if player.name != ctx.author.name:
            await ctx.send(f"Agora é a vez de {player.name}.")
            return
        if self.coup_game is None:
            await ctx.send("Nenhuma partida aberta! Use `/coup_open_game` para iniciar uma.")
            return

        player = self.coup_game.get_current_player()
        await ctx.send(f"{player.name} está pedindo Ajuda Externa, ele irá ganhar 2 tokens.")
        self.coup_game.action = "ajudaExterna"
        self.coup_game.state = "doubt"








    @commands.command()
    async def coup_test(self, ctx):
        player = self.coup_game.get_current_player()
        player.tokens += 100

async def setup(bot):
    print("Adicionando o cog CoupDiscord...")
    await bot.add_cog(CoupDiscord(bot))

if __name__ == "__main__":
    print("Este módulo não deve ser executado diretamente.")
