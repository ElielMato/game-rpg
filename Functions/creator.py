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