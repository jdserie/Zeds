
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
    if input == '1':
        






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


