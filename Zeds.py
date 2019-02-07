
import os
# UI MENU

# CODE FOR GAME
def normal():
    username = input('What is your name?\n')
    print('Bob: Hello, ' + username + '!\n' +
          'The Zeds Virus is spreading rapidly!\n' +
          'Bob: You and I have to get to the CDC safe zone on the other side of the city.\n\n'
          )
    choice_1 = input('Should we go down town[1] or through the suburbs[2]?')
    if choice_1 == '1':
        print(username + ": lets go down town!\n" +
              "Bob: Alright, Let's!\n\n" +
              'Bob: Should we go to the rooftops[1] or avoid parkour and take the Zed infested streets[2]\n\n')
        choice_2 = input('')
        if choice_2 == '1':
            print(username + ': Lets parkour across the rooftops!' +
                  'Narrator: After much parkouring,\n the duo reaches the end of the buildings\n with a low drop to the ground infront of them to a feild\n with the safe zone in sight.\n\n')
                  choice_4 = input('Feeling confident, do they decide to jump down quickly[1] or climb down the building?[2]')
            if choice_4 == '1':
                print('Narrator: The two jumped down landing on a loud bag of cans, allerting the Zeds nearby\n' +
                      'Bob: I BROKE MY LEG HELP ME UP!!!\n' +
                      username + ' noticed the Zeds approaching and left Bob and ran across the feild safely to the safe zone.'
                      )



        






# TODO: fill normal

# CODE CUT
def short():
    pass

# TODO: fill easy


def menu():
    print("Game Mode:\n" +
          "1) Short\n" +
          "2) Normal\n" +
          "3) Exit\n")


def menu_make_choice(option):
    if option == "1":
        input("*Start Game*")
        easy()

    elif option == "2":
        input("*Start Game*")
        normal()

    elif option == "3":
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


