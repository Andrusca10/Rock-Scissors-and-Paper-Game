import time
import random

global name, user
result = ["da", "d", "yes", "ye", "yep", "y", "Y", "Da", "D", "DA", "YES"]
dict ={"H": "hartie", "P": "piatra", "F": "foarfeca"}


# Functie definita pentru mesajul de introducere
def intro():
    print("Piatra, hartie, foarfeca! ")
    time.sleep(1)
    print("Salut! Eu sunt Robo. Hai sa ne jucam. " + "☺")
    time.sleep(1)


intro()


# Functie pentru introducerea numelui de la tastatura
def namefunction():
    global name, user
    name = input("Introdu numele tau: ").upper()
    time.sleep(1)


namefunction()

# Functie definita pentru implementarea jocului
def startgame():
    user = input(name + ", " + "alege-ti obiectul: P(piatra), H(hartie), F(foarfeca): ").upper()
    if user == "P":
        print("Ai ales piatra.")
    elif user == "H":
        print("Ai ales hartia.")
    elif user == "F":
        print("Ai ales foarfeca.")
    else:
        print("Nu ai ales unul din cele trei obiecte!")
    op = ["P", "H", "F"]
    robo = random.choice(op)

    if user == "P":
        if robo == "H":
            print("Ai pierdut! Computerul  a ales " + dict["H"] + " si ti-a acoperit piatra cu hartia.")
        elif robo == "F":
            print("Computerul a ales " + dict["F"] + "." + "Ai castigat! Ai zdrobit foarfeca computerului.")
    if user == "H":
        if robo == "P":
            print("Computerul a ales:" + dict["P"] + "."+ "Ai castigat! Ai acoperit piatra computerului.")
        elif robo == "F":
            print("Computerul a ales:" + dict["F"] + "." + "Ai pierdut! Computerul ti-a taiat hartia.")
    if user == "F":
        if robo == "P":
            print("Computerul a ales:" + dict["P"] + "." + "Ai pierdut! Computerul ti-a zdrobit foarfeca.")
        elif robo == "H":
            print("Computerul a ales:" + dict["H"] + "Ai castigat! Ai taiat hartia computerlui.")
    if user == robo:
        print("Ati ales acelasi obiect!")
        return


startgame()


def play_again():
    test = input("Vrei sa te mai joci? ")
    for i in range(len(result)):
        if test == result[i]:
            return startgame()
    else:
        print("La revedere!")
        time.sleep(1)


play_again()
