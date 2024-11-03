class Player:
    def __init__(self, name, user_id):
        self.name = name
        self.tokens = 2
        self.cards = []
        self.alive = True
        self.id = user_id

    def lose_card(self, card_name):
        for card in self.cards:
            if card.name == card_name:
                card.appear = True
                return card
        return None
    
    def __str__(self):
        return f"Player: {self.name} | Tokens: {self.tokens} | Cards: [{self.get_cards()}] | Alive: {self.alive}"
    
    def get_cards(self):
        status_list = []
        for i, card in enumerate(self.cards):
            status = "Morta" if card.appear else "Viva"
            status_list.append(f"{card.name} ({i} | {status})")
        return " , ".join(status_list)