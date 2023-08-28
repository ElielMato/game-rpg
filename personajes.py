class Character:
    def __init__(self, name = "", type = "", health = int(0), damage = int(0), accuracy = int(0)):
        self.name = name
        self.type = type
        self.health = health
        self.damage = damage
        self.level = 1
        self.accuracy = accuracy
        self.abilities = ["Golpeo", "Habilidad 2", "Habilidad 3"]
        self.armor = 0
        self.diamonds = 150
        self.weapon = None
        self.mana = 100


class Enemies:
    def __init__(self, name = "", health = int(0), damage = int(0), accuracy = int(0), difficulty = ""):
        self.name = name
        self.health = health
        self.damage = damage
        self.accuracy = accuracy
        self.abilities = ["Golpeo", "Habilidad 2", "Habilidad 3"]
        self.mana = 100
        self.difficulty = difficulty

class Abilities:
    def __init__(self, name = "", type = "", damage = int(0), accuracy = int(0), less_mana = int(0)):
        self.name = name
        self.type = type
        self.damage = damage
        self.accuracy = accuracy
        self.less_mana = less_mana
        
class Objects:
    def __init__(self, name = "", type = "", price = int(0), attribute_value = int(0)):
        self.name = name
        self.type = type
        self.price = price
        self.attribute_value = attribute_value
                

class Dungeons:
    def __init__(self, name = "", level = int(0)):
        self.name = name
        self.level = level

name = ""
main_character = None
guerrero = Character(name, "Guerrero", 100, 15, 50)
mago = Character(name, "Mago", 110, 10, 70)
arquero = Character(name, "Arquero", 90, 15, 75)
caballero = Character(name, "Caballero", 120, 25, 35)

def character_introduction():
    print("explicacion tipos de personajes")
    print(guerrero)
    print(mago)
    print(arquero)
    print(caballero)


def character_creator():
    type = input("Elige que tipo de personajes utilizaras:\n1) Guerrero\n2) Mago\n3) Arquero\n4) Caballero")
    if type == "1":
        guerrero.name = name
        main_character = guerrero
    elif type == "2":
        mago.name = name
        main_character = mago
    elif type == "3":
        arquero.name = name
        main_character = arquero
    elif type == "4":
        caballero.name = name
        main_character = caballero
    else:
        print("Esa opcion no esta disponible, escriba un numero del 1 al 4.")
        character_creator()
        
# Habilidades para el Mago
mage_abilities = [
    Abilities("Bola de Fuego", "Mago", 40, 80, 50),
    Abilities("Escudo Arcano", "Mago", 0, 20, 30),
    Abilities("Rayo de Hielo", "Mago", 30, 85, 40),
    Abilities("Explosión Arcana", "Mago", 50, 70, 60),
    Abilities("Curación Mística", "Mago", 30, 90, 70),
    Abilities("Descarga", "Mago", 30, 30, 20),
    Abilities("Toque de Energía", "Mago", 20, 95, 25),
    Abilities("Drenar Mana", "Mago", 0, 75, 40),
    Abilities("Espejo de Escarcha", "Mago", 0, 60, 50),
    Abilities("Nova Arcana", "Mago", 60, 80, 70)
]

# Habilidades para el Guerrero
warrior_abilities = [
    Abilities("Ataque Frenético", "Guerrero", 60, 70, 0),
    Abilities("Golpe Definitivo", "Guerrero", 80, 50, 20),
    Abilities("Embate", "Guerrero", 40, 85, 30),
    Abilities("Corte Rápido", "Guerrero", 30, 90, 25),
    Abilities("Ira del Guerrero", "Guerrero", 70, 60, 40),
    Abilities("Protección", "Guerrero", 0, 30, 20),
    Abilities("Ataque Giratorio", "Guerrero", 45, 75, 35),
    Abilities("Grito de Batalla", "Guerrero", 0, 80, 15),
    Abilities("Rugido Intimidante", "Guerrero", 0, 80, 25),
    Abilities("Embiste", "Guerrero", 55, 65, 30)
]

# Habilidades para el Caballero
knight_abilities = [
    Abilities("Lanza de Justicia", "Caballero", 50, 85, 0),
    Abilities("Escudo Protector", "Caballero", 0, 20, 40),
    Abilities("Carga Heroica", "Caballero", 65, 75, 30),
    Abilities("Golpe de Escudo", "Caballero", 35, 90, 25),
    Abilities("Promesa del Caballero", "Caballero", 0, 30, 20),
    Abilities("Juicio Divino", "Caballero", 70, 60, 45),
    Abilities("Honor del Caballero", "Caballero", 0, 80, 15)3,
    Abilities("Rendición", "Caballero", 0, 80, 30),
    Abilities("Emblema de Valor", "Caballero", 0, 70, 20),
    Abilities("Desafío", "Caballero", 0, 95, 25)
]

# Habilidades para el Arquero
archer_abilities = [
    Abilities("Disparo Preciso", "Arquero", 30, 95, 0),
    Abilities("Flecha Venenosa", "Arquero", 20, 75, 25),
    Abilities("Lluvia de Flechas", "Arquero", 45, 80, 35),
    Abilities("Tiro a la Cabeza", "Arquero", 55, 70, 30),
    Abilities("Reflejos Agudos", "Arquero", 0, 40, 20),
    Abilities("Doble Disparo", "Arquero", 25, 90, 20),
    Abilities("Flecha Explosiva", "Arquero", 60, 60, 40),
    Abilities("Flecha Paralizante", "Arquero", 10, 85, 30),
    Abilities("Flecha Distorsionante", "Arquero", 40, 75, 25),
    Abilities("Ojo de Halcón", "Arquero", 0, 80, 15)
]

def Upgrade():
    pass