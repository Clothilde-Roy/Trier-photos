import os

with open("a_sup.txt", "r") as file:
    a_sup = []
    for ligne in file:
        a_sup.append(ligne.replace("\n",""))

    for i in a_sup:
        os.remove(i)

os.remove("a_sup.txt")

