
import os
# UI MENU

# CODE FOR GAME
def normal():


# TODO: fill normal

# CODE CUT
def easy():


# TODO: fill easy


def menu():
    print("Gamemode:\n" +
          "1) Short\n" +
          "2) Normal\n" +
          "3) Exit\n")


def make_choice(option):
    if option == "1":
        easy()

    elif option == "2":
        normal()

    elif option == "3":
        exit()

    else:
        print('Syntax Error\n')



while True:
    os.system('cls||clear')

    menu()

    option = input("\n>")

    make_choice(option)

    input("*Start Game*")
