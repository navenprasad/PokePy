from Pokemon import *
from Trainer import Trainer



class Battle(object):
    def __init__(self, trainer1_name, trainer2_name):
        ash = Trainer(trainer1_name)
        misty = Trainer(trainer2_name)

        pika = Pikachu()
        char = Charmander()
        bulb = Bulbasaur()
        ash.add_pokemon(char)
        misty.add_pokemon(pika)
        misty.add_pokemon(bulb)

        ash.make_move(0, misty, 0, "tackle")
        pika.status()
        ash.show_all_pokemon()
        misty.show_all_pokemon()

        misty.make_move(0, ash, 0, "thunder_shock")
        char.status()

        ash.show_all_pokemon()
        misty.show_all_pokemon()
