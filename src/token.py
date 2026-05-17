# token.py

class Token:
    COLORS = ["red", "blue", "violet", "yellow", "green", "purple"]
    RARITIES = ["common", "rare", "legendary"]

    def __init__(self, color, rarity="common"):
        if color.lower() in self.COLORS:
            self.color = color.lower()
        else:
            raise ValueError(f"Invalid color: {color}")
        if rarity in self.RARITIES:
            self.rarity = rarity
        else:
            raise ValueError(f"Invalid rarity: {rarity}")
