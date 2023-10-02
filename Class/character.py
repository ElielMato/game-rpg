class Character:
    def __init__(self, name = "", type = "", health = int(0) , accuracy = int(0)):
        self.name = name
        self.type = type
        self.health = health
        self.level = 1
        self.accuracy = accuracy
        self.abilities = ["Golpeo", "Habilidad 2", "Habilidad 3"]
        self.armor = 0
        self.diamonds = 150
        self.weapon = None
        self.mana = 100