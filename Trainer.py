from Pokemon import *

class Trainer(object):
    name = "Unnamed Trainer"

    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self,pokemon):
        self.pokemons.append(pokemon)

    def show_all_pokemon(self):
        all_pokemon = self.pokemons
        print self.name + "'s Pokemon: "
        for pokemon in all_pokemon:
            print pokemon.name
            print pokemon.hp

        print '-----------------------------'

    def make_move(self,my_pokemon_index, trainer, enemy_pokemon_index, move):
        self.pokemons[my_pokemon_index].attack(trainer.pokemons[enemy_pokemon_index], move)
