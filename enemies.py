import random

class Enemies:
    def __init__(self, name = "", health = int(0), difficulty = ""):
        self.name = name
        self.health = health
        self.abilities = ["Golpeo", "Habilidad 2", "Habilidad 3"]
        self.difficulty = difficulty

easy_enemies = [
    Enemies(name = "Escurridizo", health = 60, difficulty = "Fácil"),
    Enemies(name = "Acechador", health = 50, difficulty = "Fácil"),
    Enemies(name = "Zumbador", health = 65, difficulty = "Fácil"),
    Enemies(name = "Sombrío", health = 50, difficulty = "Fácil"),
    Enemies(name = "Saltarín", health = 60, difficulty = "Fácil")
] 

intermediate_enemies = [
    Enemies(name = "Guardián", health = 70, difficulty = "Intermedio"),
    Enemies(name = "Traidor", health = 75, difficulty = "Intermedio"),
    Enemies(name = "Intrépido", health = 70, difficulty = "Intermedio"),
    Enemies(name = "Serpenteante", health = 75, difficulty = "Intermedio"),
    Enemies(name = "Afilado", health = 70, difficulty = "Intermedio")
]

hard_enemies = [
    Enemies(name = "Demonio", health = 80, difficulty = "Difícil"),
    Enemies(name = "Voraz", health = 85, difficulty = "Difícil"),
    Enemies(name = "Frenético", health =  80, difficulty = "Difícil"),
    Enemies(name = "Acero Negro", health = 85, difficulty = "Difícil"),
    Enemies(name = "Sombra Profunda", health = 80, difficulty = "Difícil")
]

bosses = [
    Enemies(name = "Emperador Oscuro", health = 120, difficulty = "Jefe"),
    Enemies(name = "Pesadilla Ancestral", health = 150, difficulty = "Jefe"),
    Enemies(name = "Destructor de Mundos", health = 130, difficulty = "Jefe"),
    Enemies(name = "Titán Enfurecido", health = 120, difficulty = "Jefe"),
    Enemies(name = "Eterno Desafío", health = 130, difficulty = "Jefe")
]

def enemy_chooser(difficulty):
    enemy = None
    if difficulty == "easy":
        enemy = random.choice(easy_enemies)
    elif difficulty == "intermediate":
        enemy = random.choice(intermediate_enemies)
    elif difficulty == "hard":
        enemy = random.choice(hard_enemies)
    else:
        enemy = random.choice(bosses)
    return enemy
        