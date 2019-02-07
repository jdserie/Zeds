
import os
# UI MENU

# CODE FOR GAME
def normal():
    print('cat')

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


