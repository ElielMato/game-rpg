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


class Enemies:
    def __init__(self, name = "", health = int(0), difficulty = ""):
        self.name = name
        self.health = health
        self.abilities = ["Golpeo", "Habilidad 2", "Habilidad 3"]
        self.mana = 100
        self.difficulty = difficulty

class Abilities:
    def __init__(self, name = "", type = "", damage = int(0), accuracy = int(0), less_mana = int(0)):
        self.name = name
        self.type = type
        self.damage = damage #Subir Vida o Armadura
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
guerrero = Character(name, "Guerrero", 100)
mago = Character(name, "Mago", 110)
arquero = Character(name, "Arquero", 90)
caballero = Character(name, "Caballero", 120)

def character_introduction():
    print("Informacion de los Personajes a elegir:")
    
    

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


# Habilidad Default
Abilities("Golpeo", "All", 25, 0, 20)

# Habilidades para el Guerrero
warrior_abilities = [
    Abilities("Ataque Frenético", "Guerrero", 60, 0, 30),
    Abilities("Golpe Definitivo", "Guerrero", 80, 0, 20),
    Abilities("Embate", "Guerrero", 40, 0, 30),
    Abilities("Corte Rápido", "Guerrero", 30, 0, 25),
    Abilities("Ira del Guerrero", "Guerrero", 70, 0, 40),
    Abilities("Protección", "Guerrero", 30, 100, 20), #Armadura
    Abilities("Ataque Giratorio", "Guerrero", 45, 0, 35),
    Abilities("Grito de Batalla", "Guerrero", 45, 100, 0), #Mana
    Abilities("Rugido Intimidante", "Guerrero", 50, 100, 25), #Vida
    Abilities("Embiste", "Guerrero", 55, 0, 30)
]


# Habilidades para el Mago
mage_abilities = [
    Abilities("Bola de Fuego", "Mago", 40, 0, 50),
    Abilities("Escudo Arcano", "Mago", 20, 100, 30), #Armadura
    Abilities("Rayo de Hielo", "Mago", 30, 0, 40),
    Abilities("Explosión Arcana", "Mago", 50, 0, 60),
    Abilities("Curación Mística", "Mago", 30, 0, 70),
    Abilities("Descarga", "Mago", 30, 0, 20),
    Abilities("Toque de Energía", "Mago", 20, 0, 25),
    Abilities("Drenar Mana", "Mago", 50, 100, 0), #Mana
    Abilities("Espejo de Escarcha", "Mago", 35, 100, 50), #Vida
    Abilities("Nova Arcana", "Mago", 60, 100, 50) #Vida
]

# Habilidades para el Caballero
knight_abilities = [
    Abilities("Lanza de Justicia", "Caballero", 50, 0, 0),
    Abilities("Escudo Protector", "Caballero", 30, 100, 40), #Armadura
    Abilities("Carga Heroica", "Caballero", 65, 0, 30),
    Abilities("Golpe de Escudo", "Caballero", 35, 0, 25),
    Abilities("Promesa del Caballero", "Caballero", 40, 100, 0), #Mana
    Abilities("Juicio Divino", "Caballero", 70, 0, 45),
    Abilities("Honor del Caballero", "Caballero", 0, 30, 15),
    Abilities("Rendición", "Caballero", 80, 100, 60), #Vida
    Abilities("Emblema de Valor", "Caballero", 30, 30, 20),
    Abilities("Desafío", "Caballero", 20, 100, 0) #Mana
]

# Habilidades para el Arquero
archer_abilities = [
    Abilities("Disparo Preciso", "Arquero", 30, 0, 0),
    Abilities("Flecha Venenosa", "Arquero", 20, 0, 25),
    Abilities("Lluvia de Flechas", "Arquero", 45, 0, 35),
    Abilities("Tiro a la Cabeza", "Arquero", 55, 0, 30),
    Abilities("Reflejos Agudos", "Arquero", 40, 100, 0), #Mana
    Abilities("Doble Disparo", "Arquero", 25, 0, 20),
    Abilities("Flecha Explosiva", "Arquero", 60, 0, 40),
    Abilities("Flecha Paralizante", "Arquero", 10, 0, 30),
    Abilities("Flecha Distorsionante", "Arquero", 40, 0, 25),
    Abilities("Ojo de Halcón", "Arquero", 80, 80, 100)
]

enemy_abilities = [
    Abilities("Golpe Rápido", "Enemigo", 30, 90),
    Abilities("Ataque Sorpresa", "Enemigo", 25, 80),
    Abilities("Arañazo", "Enemigo", 15, 95),
    Abilities("Mordisco", "Enemigo", 25, 85),
    Abilities("Lanzamiento de Escombros", "Enemigo", 40, 75),
    Abilities("Picotazo", "Enemigo", 20, 90),
    Abilities("Embiste", "Enemigo", 25, 80),
    Abilities("Garras Filosas", "Enemigo", 30, 85),
    Abilities("Aliento Venenoso", "Enemigo", 50, 90),
    Abilities("Ataque Desesperado", "Enemigo", 45, 70),
]

def upgrade():
    pass

#Enemigos
enemigo_facil_1 = Enemies("Escurridizo", 100, "Fácil")
enemigo_facil_2 = Enemies("Acechador", 110, "Fácil")
enemigo_facil_3 = Enemies("Zumbador", 95, "Fácil")
enemigo_facil_4 = Enemies("Sombrío", 120, "Fácil")
enemigo_facil_5 = Enemies("Saltarín", 105, "Fácil")

enemigo_intermedio_1 = Enemies("Guardián", 180, "Intermedio")
enemigo_intermedio_2 = Enemies("Traidor", 170, "Intermedio")
enemigo_intermedio_3 = Enemies("Intrépido", 190, "Intermedio")
enemigo_intermedio_4 = Enemies("Serpenteante", 160, "Intermedio")
enemigo_intermedio_5 = Enemies("Afilado", 175, "Intermedio")

enemigo_dificil_1 = Enemies("Demonio", 250, "Difícil")
enemigo_dificil_2 = Enemies("Voraz", 240, "Difícil")
enemigo_dificil_3 = Enemies("Frenético", 230, "Difícil")
enemigo_dificil_4 = Enemies("Acero Negro", 260, "Difícil")
enemigo_dificil_5 = Enemies("Sombra Profunda", 220, "Difícil")

enemigo_jefe_1 = Enemies("Emperador Oscuro", 950, "Jefe")
enemigo_jefe_2 = Enemies("Pesadilla Ancestral", 1000, "Jefe")
enemigo_jefe_3 = Enemies("Destructor de Mundos", 900, "Jefe")
enemigo_jefe_4 = Enemies("Titán Enfurecido", 920, "Jefe")
enemigo_jefe_5 = Enemies("Eterno Desafío", 980, "Jefe")

#Dugeons
dungeon1 = Dungeons("Dungeon 1", 1)
dungeon2 = Dungeons("Dungeon 2", 2)
dungeon3 = Dungeons("Dungeon 3", 3)
dungeon4 = Dungeons("Dungeon 4", 4)
dungeon5 = Dungeons("Dungeon 5", 5)

#Pociones
Object("Pociones de Vida I", "potion_heal", 400, 50)
Object("Pociones de Vida II", "potion_heal", 800, 75)
Object("Pociones de Mana I", "potion_mana", 200, 50)
Object("Pociones de Mana II", "potion_mana", 400, 75)
Object("Pociones de Armor I", "potion_armor", 600, 50)
Object("Pociones de Mana II", "potion_armor", 1200, 100)
Object("Estofado", "food_heal", 300, 40)
Object("Filete", "food_heal", 200, 30)
Object("Pan", "food_heal", 150, 25)