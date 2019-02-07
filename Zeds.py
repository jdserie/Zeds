'''
import os


'''
We want a menu:
-Add students to a list
-List all students
-Clear the list
-Exit
'''

'''
Steps to achieve goals mentioned above:
1. write directional notes like listed above
2. Write very basic code for each requirements using: prints, variables, etc... (Look at the bottom notes for example)
        (create base pieces)
3. add IMPORTS (set extra needed base pieces)
4. write code in each step without creating DEF functions (set unorganized pieces)
5. create DEF's with step 3's code (set organized pieces)
6. organize DEF's at the end of section AND lists if needed (link organized pieces)
'''


def prompt():
    print("Student Manager:\n" +
          "1) Add student\n" +
          "2) List student\n" +
          "3) Clear list\n" +
          "4) Exit")


def make_choice(option):
    if option == "1":
        tmp = input("Student's name: ")
        students.append(tmp)
        print("")

    elif option == "2":
        for student in students:
            print(student)

    elif option == "3":
        students.clear()
        print("")

    elif option == "4":
        exit()

    else:
        print('Syntax Error\n')


students = []

while True:
    os.system('cls||clear')

    prompt()

    option = input("\n>")

    make_choice(option)

    input("*Continue*")


'''
students.append("Joshua")
students.append("Josiah")
students.append("Joseph")

for student in students:        #TODO: unpacks STUDENTS to show in a list, with no box, through STUDENT
    print(student)

students.clear()

exit()
'''



'''