from comparaison import *
import PIL.Image
import time
from datetime import timedelta


path = ""
annee = ""
extension = []


# Main

fichiers = lister_fichier(path+annee, extension)

nb_fichier = len(fichiers)
print(nb_fichier)

a_sup = []

for i in range(nb_fichier):
    
    print("IMAGE N°"+str(i+1)+" sur "+str(nb_fichier))
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

for i in a_sup:
    os.remove(i)
print("Images supprimées")
