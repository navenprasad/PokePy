class Pokemon(object):
    name = "Untitled"
    hp = 0
    moves = {}
    def __init__(self, name, hp, moves):
        self.name = name
        self.hp = hp
        self.moves = moves

    def attack(self, enemy_pokemon, move):
        damage = self.moves[move]
        enemy_pokemon.hp = enemy_pokemon.hp - damage
        print self.name + " attacked " + enemy_pokemon.name + " with " + move

    def status(self):
        print "Name: " + self.name
        print "HP: " + str(self.hp)

class Pikachu(Pokemon):

    def __init__(self):
        super(Pikachu, self).__init__("Pikachu", 100,  {"tackle": 10,"thunder_shock": 20})
        print "Pikachu created!"


class Charmander(Pokemon):


    def __init__(self):
        super(Charmander, self).__init__("Charmander", 100, {"tackle": 10,"flame_thrower": 20})
        print "Charmander created!"


class Bulbasaur(Pokemon):


    def __init__(self):
        super(Bulbasaur, self).__init__("Bulbasaur", 100, {"tackle": 10,"vine_whip": 20})
        print "Bulbasaur created!"


class Squirtle(Pokemon):


    def __init__(self):
        super(Squirtle, self).__init__("Squirtle", 100, {"tackle": 10,"vine_whip": 20})
        print "Squirtle created!"
