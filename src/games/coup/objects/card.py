class Card:
    def __init__(self, name):
        self.name = name
        self.appear = False
    
    def __str__(self):
        return f"Carta: {self.name}"