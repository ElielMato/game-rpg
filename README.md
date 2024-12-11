# Final Project - Facundo Merino & Eliel Mato

## Overview
This is the final project developed by Facundo Merino and Eliel Mato for the **Computer Engineering** course. The game is implemented using **Python** and leverages object-oriented programming concepts, including the use of classes, objects, and functions. The game allows players to explore dungeons, battle enemies, and use various abilities and objects such as armors and potions.

## Project Structure

### Main Game Script
- **game.py**: The entry point for the game. To start the game, execute this script.

### Classes
The game consists of several Python classes, each representing different elements within the game:

- **abilities.py**: Contains the `Ability` class, which defines the various abilities available to characters in the game. Each ability can be used in combat, and each has unique effects.
  
- **character.py**: Contains the `Character` class. It defines the attributes and behaviors of game characters, including their health, attack, defense, and experience points. Characters can use abilities, equip items, and engage in combat.
  
- **dungeons.py**: Defines the `Dungeon` class, representing the different dungeons players can explore. Dungeons contain enemies and objects that players can interact with.
  
- **enemies.py**: Contains the `Enemy` class, which represents the enemies players will encounter during their adventure. Each enemy has different attributes like health, attack, and special abilities.
  
- **objects.py**: Defines the `Object` class, which includes various items such as armor and potions. Players can find or purchase these items to help them in their journey.

### Functions
- **functions.py**: This file contains all the helper functions required to manage the game. It includes functions for battle mechanics, inventory management, player movement, and game progression.
