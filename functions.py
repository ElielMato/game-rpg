import random
import time
from character import Character
from abilities import enemy_abilities
from dungeons import dungeon1, dungeon2, dungeon3, dungeon4, dungeon5
from abilities import Abilities
from objects import armor, potion
from enemies import Enemies

player_name = None
player_character = None
player_progress = 0
dungeon_progress = 0

def introduction():
    global player_name
    print("¡Bienvenidos aventurero! Adéntrate en un mundo lleno de misteriosas mazmorras, donde la valentía y la estrategia son tus mejores aliados. ¡Forja tu leyenda enfrentando a peligrosos enemigos y conquistando cada nivel de las mazmorras!")
    time.sleep(4)
    player_name = input("¿Como te llamas?: ")
    print("¡Bienvenido", player_name, "!")
    time.sleep(3)
    
def character_introduction():
    guerrero = Character(type = "Guerrero")
    mago = Character(type = "Mago")
    arquero = Character(type = "Arquero")
    caballero = Character(type = "Caballero")
    print("Elige tu destino: guerrero, mago, arquero o caballero. Tu elección define tu camino en la batalla y tu estrategia. ¡Adéntrate en esta aventura y elige con sabiduría!")
    time.sleep(5)
    print(guerrero)
    time.sleep(5)
    print(mago)
    time.sleep(5)
    print(arquero)
    time.sleep(5)
    print(caballero)
    time.sleep(5)
    character_creator()
    
def character_creator():
    global player_character
    global player_name
    type = input("Elige que tipo de personajes utilizaras:\n1) Guerrero\n2) Mago\n3) Arquero\n4) Caballero\nNumero de personaje: ")
    if type == "1":
        player_character = Character(name = player_name, type = "Guerrero", health = 100)
        print("¡Estamos listo para la batalla!")
        time.sleep(2)
        print("Estamos dirigiéndonos hacia tu refugio. Aquí puedes prepararte para tu próxima aventura, forjar tu destino con el herrero o explorar el poder de la magia con el hechicero.")
        time.sleep(3)
    elif type == "2":
        player_character = Character(name = player_name, type = "Mago", health = 110)
        print("¡Estamos listo para la batalla!")
        time.sleep(2)
        print("Estamos dirigiéndonos hacia tu refugio. Aquí puedes prepararte para tu próxima aventura, forjar tu destino con el herrero o explorar el poder de la magia con el hechicero.")
        time.sleep(3)
    elif type == "3":
        player_character = Character(name = player_name, type = "Arquero", health = 90)
        print("¡Estamos listo para la batalla!")
        time.sleep(2)
        print("Estamos dirigiéndonos hacia tu refugio. Aquí puedes prepararte para tu próxima aventura, forjar tu destino con el herrero o explorar el poder de la magia con el hechicero.")
        time.sleep(3)
    elif type == "4":
        player_character = Character(name = player_name, type = "Caballero", health = 120)
        print("¡Estamos listo para la batalla!")
        time.sleep(2)
        print("Estamos dirigiéndonos hacia tu refugio. Aquí puedes prepararte para tu próxima aventura, forjar tu destino con el herrero o explorar el poder de la magia con el hechicero.")
        time.sleep(3)
    else:
        print("Esa opcion no esta disponible, vuelve a intentarlo")
        time.sleep(2)
        character_creator()

def herrero():
    global player_character
    print("¡Bienvenido a mi taller de herreria, aqui puedes encontrar todo tipo de articulos utiles para la batalla!")
    time.sleep(3)
    print("Esto es lo que tengo hoy para ti:")
    time.sleep(2)
    armor_selection = random.choice(armor)
    print(armor_selection.name, ":", armor_selection.description)
    print("Proteccion:", armor_selection.attribute_value)
    print("Coste:", armor_selection.price, "diamantes")
    time.sleep(3)
    print("¿Deseas comprarlo?")
    print("Diamantes disponibles:", player_character.diamonds)
    print(
        '''
1) Si
2) No (volver al menu principal)
        
        '''
        )    
    choice = int(input("Elige la opcion a realizar (numero): "))
    if choice == 1:
        if player_character.diamonds >= armor_selection.price:
            print("¡Compra realizada con exito!")
            time.sleep(3)
            player_character.diamonds = player_character.diamonds - armor_selection.price
            player_character.armor = armor_selection.attribute_value
            menu()
        else:
            print("No tienes suficientes diamantes, vuelve mas tarde")
            time.sleep(3)
            menu()
            
    else:
        print("Lamento que no hayamos llegado a un acuerdo, ¡vuelve cuando quieras!")
        time.sleep(3)
        menu()

def hechizero():
    global player_character
    print("¡Bienvenido aventurero, aquí encontrarás elementos místicos para potenciar tus ataques y adentrarte en el mundo de la magia!")
    time.sleep(3)
    print("Esto es lo que tengo hoy para ti:")
    time.sleep(2)
    potion_selection = random.choice(potion)
    print(potion_selection.name, ":", potion_selection.description)
    print("Multiplicador de daño:", potion_selection.attribute_value)
    print("Coste:", potion_selection.price, "diamantes")
    time.sleep(3)
    print("¿Deseas comprarlo?")
    print("Diamantes disponibles:", player_character.diamonds)
    print(
        '''
1) Si
2) No (volver al menu principal)
        
        '''
        )    
    choice = int(input("Elige la opcion a realizar (numero): "))
    if choice == 1:
        if player_character.diamonds >= potion_selection.price:
            print("¡Compra realizada con exito!")
            time.sleep(3)
            player_character.diamonds = player_character.diamonds - potion_selection.price
            player_character.potion = potion_selection.attribute_value
            menu()
        else:
            print("No tienes suficientes diamantes, vuelve mas tarde")
            time.sleep(3)
            menu()
            
    else:
        print("Lamento que no hayamos llegado a un acuerdo, ¡vuelve cuando quieras!")
        time.sleep(3)
        menu()

def inventory():
    global player_character
    print("INVENTARIO:")
    print("Diamantes:", player_character.diamonds)
    print("Proteccion de armadura:", player_character.armor)
    print("Multiplicador de ataque (pociones):", player_character.potion)
    time.sleep(5)
    menu()
    
def menu():
    print("REFUGIO")
    print(
        '''
1) Jugar
2) Herrero
3) Hechizero
4) Inventario
        '''
        )
    player_choice = int(input("Elige la opcion a realizar: "))
    if player_choice == 1:
        game()
    elif player_choice == 2:
        herrero()
    elif player_choice == 3:
        hechizero()
    elif player_choice == 4:
        inventory()
    else:
        print("Esta opcion no esta disponible, vuelve a intentarlo")
        time.sleep(2)
        menu()   
        
        
def game():
    global player_progress
    global dungeon_progress
    current_dungeon = None
    
    
    dungeons = [dungeon1, dungeon2, dungeon3, dungeon4, dungeon5]
    current_dungeon = dungeons[player_progress]
    dungeon_progress = int(0)
    print(f"¡Bienvenido a la mazmorra: {current_dungeon.name}!")
    time.sleep(3)

        
    while dungeon_progress < 5:  
        if dungeon_progress == 4:
            print("¡Has llegado al jefe final!")
            enemy = current_dungeon.enemies[4]
            attack(enemy)
        else:
            enemy = current_dungeon.enemies[dungeon_progress]
            print(f"Nivel {dungeon_progress + 1}: {enemy.name}")
            time.sleep(3)
            attack(enemy)

    print("¡Has completado todas las mazmorras!")
    time.sleep(3)
    menu()
                
def player_attack_chooser():
    while True:
        print("ATAQUES DISPONIBLES:")
        print("1)", player_character.abilities[0].name, "Daño:", player_character.abilities[0].damage)
        print("2)", player_character.abilities[1].name, "Daño:", player_character.abilities[1].damage)
        print("3)", player_character.abilities[2].name, "Daño:", player_character.abilities[2].damage)
        choice = int(input("Elige el ataque que deseas realizar (numero): "))
        
        if choice == 1:
            return player_character.abilities[0]
        elif choice == 2:
            return player_character.abilities[1]
        elif choice == 3:
            return player_character.abilities[2]
        else:
            print("Esta opción no está disponible, vuelve a intentarlo")
            time.sleep(2)
                           
def attack(enemy):
    global player_character
    global player_progress
    global dungeon_progress
    player_health = player_character.health  
    enemy_health = enemy.health  
    
    while player_health > 0 and enemy_health > 0:
        print("JUGADOR:", player_character.name)
        print("VIDA RESTANTE:", player_health)
        print("ENEMIGO:", enemy.name)
        print("VIDA RESTANTE:", enemy_health)
        player_attack = player_attack_chooser()
        print("Ataque elegido:", player_attack.name)
        time.sleep(2)
        enemy_attack = random.choice(enemy_abilities)
        print("3... 2... 1...")
        time.sleep(2)
        player_damage = player_attack.damage * player_character.potion
        enemy_health = enemy_health - player_damage  
        print("¡Ataque realizado con éxito!")
        time.sleep(2)
        print("El enemigo responde con:", enemy_attack.name)
        enemy_damage = enemy_attack.damage - player_character.armor
        player_health = player_health - enemy_damage 
        time.sleep(2)
        print("Daño recibido:", enemy_damage)
        time.sleep(2)

    if player_health <= 0:
        print("¡Has muerto!")
        time.sleep(2)
        print("El fin llega, pero la aventura sigue. ¡Prepárate y vuelve a intenarlo!")
        time.sleep(3)
        dungeon_progress = 0
        player_progress = player_progress
        menu()
    else:
        print(f"¡Has derrotado a {enemy.name}!")
        time.sleep(2)
        dungeon_progress += 1
        if dungeon_progress < 5:
            print(f"Progreso en la mazmorra: {dungeon_progress + 1} de 5")
            time.sleep(3)
        else:
            print("¡Has completado la mazmorra!")
            time.sleep(2)
            player_progress += 1
            dungeon_progress = 0
            player_character.diamonds = player_character.diamonds + 200
            print("Premio: 150 diamantes")
            time.sleep(3)
            menu()
