from enemies import enemy_chooser

class Dungeons:
    def __init__(self, name = "", enemies = None):
        self.name = name
        if enemies is None:
            self.enemies = []
        else:
            self.enemies = enemies


dungeon1 = Dungeons("Criptas olvidadas", [enemy_chooser("easy"), enemy_chooser("easy"), enemy_chooser("easy"), enemy_chooser("intermediate"), enemy_chooser("boss")])
dungeon2 = Dungeons("Abismo de las almas", [enemy_chooser("easy"), enemy_chooser("intermediate"), enemy_chooser("intermediate"), enemy_chooser("hard"), enemy_chooser("boss")])
dungeon3 = Dungeons("Ruinas ancestrales", [enemy_chooser("intermediate"), enemy_chooser("intermediate"), enemy_chooser("hard"), enemy_chooser("hard"), enemy_chooser("boss")])
dungeon4 = Dungeons("Cripta de las sombras", [enemy_chooser("intermediate"), enemy_chooser("hard"), enemy_chooser("hard"), enemy_chooser("hard"), enemy_chooser("boss")])
dungeon5 = Dungeons("Abismo maldito", [enemy_chooser("hard"), enemy_chooser("hard"), enemy_chooser("hard"), enemy_chooser("hard"), enemy_chooser("boss")])