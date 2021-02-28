#!usr/bin/env python3
import os
import time
os.system("clear")
banner = ("\n~ C a l c u l a t r i c e\n")
print(banner)
while True:
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le deuxième nombre : "))
    c = input("Entrez l'opération que vous voulez effectuer (multiplication (m/M) | addition (a/A) | soustraction (s/S) | division (d/D)) : ")

    if c == "multiplication" or c == "m" or c == "M":
        resultat = a * b
        print("Le résultat de la multiplication de ces deux nombres est ")
        print(resultat)
    if c == "addition" or c == "a" or c == "A":
        resultat = a + b
        print("Le résultat de l'addition de ces deux nombres est")
        print(resultat)
    if c == "soustraction" or c == "s" or c == "S":
        resultat = a - b
        print("Le résultat de la soustraction de ces deux nombres est")
        print(resultat)
    if c == "division" or c == "d" or c == "D":
        resultat = a / b
        print("Le résultat de la division de ces deux nombres est : ")
        print(resultat)

    restart = input("Voulez vous continuer? (Y/N) : ")
    if restart == "y" or restart == "Y":
        print(banner)
        pass
    elif restart == "n" or restart == "N":
        print("Vous avez quitté la calculatrice")
        time.sleep(3)
        break
