from comparaison import *
import PIL.Image
import time
from datetime import timedelta

# path = "/Users/clothilde.royan/Desktop/dossier sans titre/"
path = "/Users/clothilde.royan/Desktop/image/"
annee = "2008/"

# Main
extension = ['jpg', 'JPG', 'jpeg']
fichiers = lister_fichier(path+annee, extension)
# print(fichiers)

nb_fichier = len(fichiers)
print(nb_fichier)

a_sup = []

for i in range(nb_fichier):
    print("IMAGE N°"+str(i+1))
    start_time = time.monotonic()
    if path+annee+fichiers[i] not in a_sup:
        for j in range(i + 1, nb_fichier):

            image_1 = PIL.Image.open(path+annee+fichiers[i])
            image_2 = PIL.Image.open(path+annee+fichiers[j])
            comp = comparaison(image_1, image_2)

            if comp != 0:
                if path+annee+fichiers[j]not in a_sup:
                    a_sup.append(path+annee+fichiers[j])

    end_time = time.monotonic()
    print("Temps = ", timedelta(seconds=end_time - start_time))

with open("a_sup.txt", "w") as file:
    for i in a_sup:
        file.write(i+"\n")
