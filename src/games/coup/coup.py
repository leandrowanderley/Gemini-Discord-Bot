from games.coup.objects.deck import Deck
from games.coup.objects.player import Player

class Coup:
    def __init__(self, gamemode):
        self.deck = Deck(gamemode)
        self.players = []
        self.turn = None
        self.state = "waiting" # waiting / doubt
        self.cpass = None
        self.action = ""
        self.target = ""
    
    def start_game(self):
        print("INFO: Iniciando o jogo...")
        for player in self.players:
            player.cards.append(self.deck.get_card())
            player.cards.append(self.deck.get_card())

    def next_turn(self):
        self.turn = (self.turn + 1) % len(self.players)

    def add_player(self, player_name, user_id):
        for player in self.players:
            if player_name == player.name:
                print(f"ERRO: Jogador {player_name} já existe!")
                return

        player = Player(player_name, user_id)
        self.players.append(player)
        print(f"Jogador adicionado: {player.name}. Total de jogadores: {len(self.players)}")

    def get_player(self, player_name):
        return next((player for player in self.players if player.name == player_name), None)
    
    def get_players(self):
        return [player.name for player in self.players]
    
    def get_current_player(self):
        return self.players[self.turn]



    # Actions

    def action(self, player):
        if self.action == "basica":
            self.action_basica(player)
        elif self.action == "ajudaExterna":
            self.action_ajudaExterna(player)
        elif self.action == "coup":
            self.action_coup(player)
        elif self.action == "duque":
            self.action_duque(player)
        elif self.action == "capitao":
            self.action_capitao(player)
        # elif self.action == "assassino":
        #     self.action_assassino(player, target, card_name)
        # elif self.action == "embaixador":
        #     self.action_embaixador(player)

    def action_basica(self, player):
        player.tokens += 1
    
    def action_ajudaExterna(self, player):
        player.tokens += 2
    
    def action_coup(self, player):
        if player.tokens < 7:
            return False
        player.tokens -= 7

    def action_duque(self, player):
        player.tokens += 3
    
    def action_capitao(self, player):
        for i in range(len(self.players)):
            if self.players[i].name == self.target:
                target = self.players[i]
                break

        steal_amount = min(target.tokens, 2)
        if steal_amount > 0:
            target.tokens -= steal_amount
            player.tokens += steal_amount
            return True
        return False

    def action_assassino(self, player, target, card_name):
        if player.tokens < 3:
            return False
        player.tokens -= 3
        # target.lose_card(card_name)

    def action_embaixador_first(self, player):
        player.Cards.append(self.deck.get_card())
        player.Cards.append(self.deck.get_card())
        player.Cards.random.shuffle()
    
    def action_embaixador_second(self, player, card_number):
        card = player.Cards.pop(card_number)
        if card:
            self.deck.return_card(card)
    
    def action_choose_card(self, player, chosen_card):
        print(f"INFO: tentando eliminar a carta {chosen_card.name} do jogador {player.name}")

        for card in player.cards:
            if card.name == chosen_card.name and not card.appear:
                card.appear = True
                    

            print(f"INFO: Carta {chosen_card.name} eliminada do jogador {player.name}.")
            return chosen_card
        else:
            print(f"ERRO: Carta {chosen_card.name} não encontrada nas cartas do jogador {player.name}.")
            return None
        
