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
    
    def __repr__(self):
        description = ""
        if self.name == "Guerrero":
            description = "El guerrero es un luchador intrépido que se enfrenta a sus enemigos con valentía y fuerza bruta. Con su imponente fuerza, defiende la justicia y la gloria en el campo de batalla."
        elif self.name == "Mago":
            description = "El hechicero es un conjurador de secretos antiguos y magia oscura. Con su destreza en las artes ocultas, teje hechizos misteriosos que desafían las leyes de la realidad."
        elif self.name == "Caballero":
            description = "El caballero es un noble guerrero de corazón noble y valor inquebrantable. Con su armadura reluciente y su fiel espada, defiende el honor y la justicia en tiempos de peligro. Su lealtad y coraje son tan imponentes como su armadura brillante mientras cabalga en busca de aventuras y protege a los indefensos."
        else:
            description =  "El arquero es un experto tirador con una puntería excepcional. En la distancia, con su arco y flechas, es el guardián de la precisión y la velocidad, derribando a sus enemigos con elegancia mortal."
        return description

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

enemy_abilities = [
    Abilities("Golpe Rápido", "Enemigo", 30, 90),
    Abilities("Ataque Sorpresa", "Enemigo", 25, 80),
    Abilities("Arañazo", "Enemigo", 15, 95),
    Abilities("Mordisco", "Enemigo", 15, 85),
    Abilities("Lanzamiento de Escombros", "Enemigo", 40, 75),
    Abilities("Picotazo", "Enemigo", 20, 90),
    Abilities("Embiste", "Enemigo", 25, 80),
    Abilities("Garras Filosas", "Enemigo", 30, 85),
    Abilities("Aliento Venenoso", "Enemigo", 50, 90),
    Abilities("Ataque Desesperado", "Enemigo", 45, 70),
]

def Upgrade():
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

player_name = ""
player_character = None

def introduction():
    print("BIENVENIDOS A game_name!")
    print("game_name es un juego basado ")
    
def character_introduction():
    print("Informacion de los Personajes a elegir:")
    
def character_creator():
    type = input("Elige que tipo de personajes utilizaras:\n1) Guerrero\n2) Mago\n3) Arquero\n4) Caballero")
    if type == "1":
        guerrero.name = name
        player_character = guerrero
    elif type == "2":
        mago.name = name
        player_character = mago
    elif type == "3":
        arquero.name = name
        player_character = arquero
    elif type == "4":
        caballero.name = name
        player_character = caballero
    else:
        print("Esa opcion no esta disponible, escriba un numero del 1 al 4.")
        character_creator()
        
        