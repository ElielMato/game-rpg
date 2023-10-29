class Objects:
    def __init__(self, name = "", description = "", type = "", price = int(0), attribute_value = int(0)):
        self.name = name
        self.description = description
        self.type = type
        self.price = price
        self.attribute_value = attribute_value

potion = [
    Objects("Poción de Furia", "Aumenta la furia del bebedor", "Poción", 250, 1.6),
    Objects("Poción de Agresión", "Incrementa la agresión", "Poción", 150, 1.3),
    Objects("Poción de Aniquilación", "Potencia el ataque", "Poción", 300, 1.8),
    Objects("Poción de Destrucción", "Mejora el poder destructivo", "Poción", 280, 1.7),
    Objects("Poción de Velocidad Mortal", "Proporciona velocidad letal", "Poción", 200, 1.4),
    Objects("Poción de Resistencia Bélica", "Mejora la resistencia en la batalla", "Poción", 210, 1.5),
    Objects("Poción de Salud Revigorizante", "Revitaliza la salud", "Poción", 270, 1.7),
    Objects("Poción de Poder Místico", "Concede poder mágico", "Poción", 220, 1.4),
    Objects("Poción de Energía Despiadada", "Da energía sin límites", "Poción", 230, 1.5),
    Objects("Poción de Fortuna en el Ataque", "Atrae la buena fortuna para el ataque", "Poción", 260, 1.6)
]

armor = [
    Objects("Coraza del Último Suspiro", "Una armadura legendario de defensa inquebrantable", "Armadura", 500, 30),
    Objects("Manto de las Sombras", "Un manto encantado que otorga oscuridad y sigilo", "Armadura", 400, 15),
    Objects("Placas del Guerrero Valeroso", "Placas de un héroe valiente y resistente", "Armadura", 550, 30),
    Objects("Caparazón del Guardián", "Una armadura de hierro capaz de soportar embates letales", "Armadura", 600, 32),
    Objects("Yelmo del Vigía Celestial", "Yelmo que protege y vislumbra lo oculto", "Armadura", 450, 15),
    Objects("Escudo de las Mil Batallas", "Un escudo mágico de defensa indomable", "Armadura", 520, 30),
    Objects("Faja del Vencedor Incansable", "Una faja que simboliza la victoria eterna", "Armadura", 480, 20),
    Objects("Guanteletes de la Roca", "Guantes hechos de material indestructible", "Armadura", 530, 30),
    Objects("Botas del Caminante Infatigable", "Botas que permiten recorrer distancias inmensas", "Armadura", 510, 22),
    Objects("Amuleto del Escudo Divino", "Un amuleto que proyecta barreras protectoras", "Armadura", 570, 26)
]
