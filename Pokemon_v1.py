from random import *

pikachu_moves = ["thundershock", "swift", "thunder", "headbutt"]
squirtle_moves = ["dynamicpunch", "bubble", "whirlpool", "headbutt"]
charmander_moves = ["ember", "slash", "scratch", "rage"]
bulbasaur_moves = ["drain", "whip", "tackle", "sludge"]

pokemons = ["pikachu", "squirtle", 'charmander', 'bulbasaur']

pikachu_greeting = "Congratulations! You have selected the lightning rodent"
squirtle_greeting = "Congratulations! You have selected the slimy yet adorable turtle"
charmander_greeting = "Ah yes, you have chosen the flaming lizard aka Mr. Steal yo girl"
bulbasaur_greeting = "Really?! Bulbasaur? I mean c'mon. He is basically a French bulldog made out of flowers"

print("\nYou are about to play the most dank pokemon game you've ever played")
print('\nPokemon: ' + str(pokemons))
print('\n')

class Pokemon:
    def __init__(self, name, hp, speed, attack, spattack, defense, spdefense, move):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.spattack = spattack
        self.spdefense = spdefense
        self.speed = speed
        self.move = move

    def display_stats(self):
        print( 'HP is: ' + str(self.hp) + ' Speed is: ' + str(self.speed) + ' Attack is: ' + str(self.attack)+ ' Special Attack is: ' + str(self.spattack)+ ' Defense is: ' + str(self.defense)+ ' Special Defense is: ' + str(self.spdefense))

    def dynamicpunch(P1, P2):
        print(P1.name + " used dynamicpunch")
        P2.hp -= (75 + P1.attack - P2.defense)
        print(P2.name + ' got a black eye')
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    def drain(P1, P2):
        print(P1.name + " used drain")
        P2.hp -= (40 + P1.spattack - P2.spdefense)
        P1.hp += (40 + P1.spattack - P2.spdefense)
        print(P2.name + " siphoned some of " + P1.name + "'s soul")
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp, P1.hp

    def sludge(P1, P2):
        print(P1.name + " used sludge")
        P2.hp -= (65 + P1.spattack - P2.spdefense)
        print(P2.name + " got toxicly wasted")
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    def tackle(P1, P2):
        print(P1.name + " used tackle")
        P2.hp -= (40 + P1.attack - P2.defense)
        print(P2.name + ' got taken to the ground')
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    def whip(P1, P2):
        print(P1.name + " used whip")
        P2.hp -= (45 + P1.attack - P2.defense)
        print(P2.name + ' was whipped... and he liked it')
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    def scratch(P1, P2):
        print(P1.name + " used scratch")
        P2.hp -= (40 + P1.attack - P2.defense)
        print(P2.name + ' got a boo boo')
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    def slash(P1, P2):
        print(P1.name + " used slash")
        P2.hp -= (70 + P1.attack - P2.defense)
        print(P2.name + ' got a Columbian Necktie')
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    def ember(P1, P2):
        print(P1.name + " used ember")
        P2.hp -= (40 + P1.spattack - P2.spdefense)
        print(P1.name + " spit mad fire on the mic")
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    def bubble(P1, P2):
        print(P1.name + " used bubble")
        P2.hp -= (40 + P1.spattack - P2.spdefense)
        print(P2.name + " is all wet ;P")
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    def whirlpool(P1, P2):
        print(P1.name + " used whirlpool")
        P2.hp -= (35 + P1.spattack - P2.spdefense)
        print(P2.name + " got pulled into a riptide.")
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    def headbutt(P1, P2):
        print(P1.name + " used headbutt")
        P2.hp -= (70 + P1.attack - P2.defense)
        print(P2.name + ' said: That fucking hurt asshole!')
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    def thundershock(P1, P2):
        print(P1.name + " used thundershock")
        P2.hp -= (40 + P1.spattack - P2.spdefense)
        print(P2.name + " said don't taze me bro!")
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    def swift(P1, P2):
        print(P1.name + " used swift")
        P2.hp -= (60 + P1.attack - P2.defense)
        print(P2.name + ' is seeing stars')
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    def thunder(P1, P2):
        print(P1.name + " used thunder")
        P2.hp -= (75 + P1.spattack - P2.spdefense)
        print(P2.name + " was smote by " + P1.name)
        print(str(P2.name) + ' HP: ' + str(P2.hp))
        return P2.hp

    #def slaughter(P1, P2):
        #print(P1.name + " slicked the earth with the blood of " + P2.name)
        #P2.hp -= (1000000000000000000000000 + P1.spattack - P2.spdefense)
        #print(P2.name + " died screaming")
        #print(str(P2.name) + ' HP: ' + str(P2.hp))
        #return P2.hp



def choose_P1():
    Player1 = input("P1: Choose your Pokemon from the list above: ")
    if Player1.lower() == "pikachu":
        print(pikachu_greeting)
        pikachu.display_stats()
        print("Your Pikachu knows " + str(pikachu_moves))
        pokemons.remove('pikachu')
        return pikachu
    elif Player1 == "squirtle":
        print(squirtle_greeting)
        squirtle.display_stats()
        print("Your Squirtle knows " + str(squirtle_moves))
        pokemons.remove('squirtle')
        return squirtle
    elif Player1 == "bulbasaur":
        print(bulbasaur_greeting)
        bulbasaur.display_stats()
        print("Your Bulbasaur knows " + str(bulbasaur_moves))
        pokemons.remove('bulbasaur')
        return bulbasaur
    elif Player1 == "charmander":
        print(charmander_greeting)
        charmander.display_stats()
        print("Your Charmander knows " + str(charmander_moves))
        pokemons.remove('charmander')
        return charmander
    else:
        choose_P1()

def choose_P2():
    print(pokemons)
    Player2 = input("P2: Choose your Pokemon from the list above: ")
    for Player2 in pokemons:
        if Player2.lower() == "pikachu":
            print(pikachu_greeting)
            pikachu.display_stats()
            print("Your Pikachu knows " + str(pikachu_moves))
            return pikachu
        elif Player2.lower() == "squirtle":
            print(squirtle_greeting)
            squirtle.display_stats()
            print("Your Squirtle knows " + str(squirtle_moves))
            return squirtle
        elif Player2.lower() == "bulbasaur":
            print(bulbasaur_greeting)
            bulbasaur.display_stats()
            print("Your Bulbasaur knows " + str(bulbasaur_moves))
            return bulbasaur
        elif Player2.lower() == "charmander":
            print(charmander_greeting)
            charmander.display_stats()
            print("Your Charmander knows " + str(charmander_moves))
            return charmander
        else:
            choose_P2()



#individual pokemon attack
def Turn(P1, P2):
    print(P1.move)
    action = str.lower(input('What move do you use?'))
    for x in P1.move:
        if action == x:
            y = ("P1." + action + '(' + str("P2") + ')')
            eval(y)
    if action == 'slaughter':
        y = ("P1.slaughter" + '(' + str("P2") + ')')
        eval(y)

#function of two pokemon fighting

def match(P1, P2):
    if P1.speed >= P2.speed:
        while P1.hp > 0 and P2.hp > 0:
            print("\nP1's turn:")
            Turn(P1, P2)
            if P1.hp <= 0 or P2.hp <= 0:
                break
            print("\nP2's turn:")
            Turn(P2, P1)
        if P1.hp > 0:
            print("P1 wins!")
        else:
            print("P2 wins")
    else:
        while P1.hp > 0 and P2.hp > 0:
            print("\nP2's turn:")
            Turn(P2, P1)
            if P1.hp <= 0 or P2.hp <= 0:
                break
            print("\nP1's turn:")
            Turn(P1, P2)
        if P1.hp > 0:
            print("P1 wins!")
        else:
            print("P2 wins")

#main function
def battle():
    P1 = choose_P1()
    P2 = choose_P2()
    match(P1, P2)
    prompt = input("Do you want to play again?")
    if prompt.lower() == "yes" or prompt.lower() == "y":
        pikachu.hp = 100
        squirtle.hp = 90
        battle()
    else:
        print("Thanks for playing!")

charmander = Pokemon('Charmander', 146, 114, 104, 123, 112, 128, charmander_moves)
squirtle = Pokemon('Squirtle', 151, 110, 128, 112, 127, 104, squirtle_moves)
pikachu = Pokemon('Pikachu', 142, 117, 101, 112, 112, 156, pikachu_moves)
bulbasaur = Pokemon('Bulbasaur', 152, 111, 111, 128, 128, 106, bulbasaur_moves)

battle()
