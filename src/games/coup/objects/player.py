class Player:
    def __init__(self, name):
        self.name = name
        self.tokens = 2
        self.cards = []
        self.alive = True

    def lose_card(self, card_name):
        for card in self.cards:
            if card.name == card_name:
                self.cards.appear = True
                return card
        return None
    
    def __str__(self):
        return "Player: " + self.name + " Tokens: " + str(self.tokens) + " Cards: [" + self.get_cards() + "] Alive: " + str(self.Alive)
    
    def get_cards(self):
        status_list = []
        for i, card in enumerate(self.cards):
            status = "Viva" if card.appear else "Morta"
            status_list.append(f"{card.name} ({i} | {status})")
        return " , ".join(status_list)