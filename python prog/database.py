people = {"dave": "joiner", "bob": "boilder"}


def intro():
    print("wel come to data base \n")
    print("To get access enter your password")
    enter_password()


def enter_password():
    password ="123ab"
    entry1 = input("password: ")
    if (len(entry1) < 3 and (entry1 != password)):
        print("access denied")
    else:
        print("access ganarted")
        data_base()


def data_base():

    x = int(input("clear(1),update(2),print(3)"))
    if x == 1:
        people.clear()
        print(people)
        print("data base is clear")
    elif x == 2:
        update_dictionary()
    elif x == 3:
        print(people)


def update_dictionary():
    for i in range(3):
        name = input("enter name :")
        job = input("enter job : ")
        people[name] = job
        print(people)


intro()
