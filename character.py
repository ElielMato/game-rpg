from abilities import Golpeo
from abilities import ability_chooser

class Character:
    def __init__(self, name = "", type = "", health = int(0), armor = int(0)):
        self.name = name
        self.type = type
        self.health = health
        self.abilities = [Golpeo, ability_chooser(type), ability_chooser(type)]
        self.armor = 0
        self.diamonds = 150
        self.potion = 1

    def __repr__(self):
        description = ""
        if self.type == "Guerrero":
            description = "El guerrero es un luchador intrépido que se enfrenta a sus enemigos con valentía y fuerza bruta. Con su imponente fuerza, defiende la justicia y la gloria en el campo de batalla."
        elif self.type == "Mago":
            description = "El hechicero es un conjurador de secretos antiguos y magia oscura. Con su destreza en las artes ocultas, teje hechizos misteriosos que desafían las leyes de la realidad."
        elif self.type == "Caballero":
            description = "El caballero es un noble guerrero de corazón noble y valor inquebrantable. Con su armadura reluciente y su fiel espada, defiende el honor y la justicia en tiempos de peligro. Su lealtad y coraje son tan imponentes como su armadura brillante mientras cabalga en busca de aventuras y protege a los indefensos."
        else:
            description = "El arquero es un experto tirador con una puntería excepcional. En la distancia, con su arco y flechas, es el guardián de la precisión y la velocidad, derribando a sus enemigos con elegancia mortal."
        return description
    