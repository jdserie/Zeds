
import os
# UI MENU

# CODE FOR GAME
def normal():
    username = input('What is your name?\n')
    print('Bob: Hello, ' + username + '!\n' +
          'The Zeds Virus is spreading rapidly!\n' +
          'Bob: You and I have to get to the CDC safe zone on the other side of the city.\n\n'
          )
    print(username + ": lets go down town!\n" +
              "Bob: Alright, let's!\n\n")
    choice_2 = input('Bob: Should we go to the rooftops[1] or avoid parkour and take the Zed infested streets[2]?')
    if choice_2 == '1':
            print(username + ': Lets parkour across the rooftops!' +
                  'Narrator: After much parkouring,\n the duo reaches the end of the buildings\n with a low drop to the ground in front of them to a feild\n with the safe zone in sight.\n\n')
            choice_4 = input('Feeling confident, do they decide to jump down quickly[1] or climb down the building?[2]')
            if choice_4 == '1':
                print('Narrator: The two jumped down landing on a loud bag of cans, allerting the Zeds nearby\n' +
                      'Bob: I BROKE MY LEG HELP ME UP!!!\n' +
                      'Narrator: ' + username + ' noticed the Zeds approaching fast and left Bob as bait\n.' +
                        'and ran across the field safely to the Safe Zone.\n\n' +
                        "Bob's as bait was worth it!\n" + username + " survived!"
                      )
                exit()
            elif choice_4 == '2':
                print('Narrator: The duo climbed down a fire ladder quietly.\nThey ran safeley to the Safe Zone!\n\n' +
                        username + ' and Bob both survived!')
                exit()
    elif choice_2 == '2':
        print(username + ': Go down the roads! It is faster.\n\n')
        choice_3 = input('Bob: should we take that running car[1] or try to out run them?[2]')
        if choice_3 == '1':
            print('Narrator: The two ignored a rule from ZombieLand: "Check the backseat."\n' +
                          'There was a Zed back there.\nYou both died...')
            exit()
        elif choice_3 == '2':
            print('Narrator: There was way to many Zeds down that road...\nYou died.')
            exit()










        






# TODO: fill normal

# CODE CUT
def short():
    pass

# TODO: fill easy


def menu():
    print("Game Mode:\n" +
          "1) Normal\n" +
          "2) Exit\n")


def menu_make_choice(option):
    if option == "1":
        input("*Start Game*")
        normal()

    elif option == "2":
        exit()

    else:
        print('Syntax Error\n')

'''
def endgame():
    print('Game Over')
'''

while True:
    os.system('cls||clear')

    menu()

    option = input("\n>")

    menu_make_choice(option)

 #   endgame()


