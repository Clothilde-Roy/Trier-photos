import os
import PIL.Image
import numpy as np
from exifread import process_file
from datetime import datetime


def comparaison(im1, im2):
    #print("Taille 1 : ", im1.size, "Taille 2 : ", im2.size)
    if im1.size != im2.size:
        return 0
    else:
        T1 = np.array(im1)
        T2 = np.array(im2)
        for i, j in zip(T1, T2):
            if i.all() != j.all():
                return 0
        return 1

def lister_fichier(path, extension):
    fichiers = os.listdir(path)
    #print(fichiers)
    result = []
    for i in fichiers:
        ext = i.split(".")
        #print(ext)
        if len(ext) > 1:
            if ext[1] in extension:
                result.append(i)

    return result

def changer_nom(fichier, path):
    im = open(path+fichier, 'rb')
    tags = process_file(im)

    if "Image DateTime" in tags.keys():
        ext = fichier.split(".")
        date = str(tags["Image DateTime"]).replace(":", "_").replace(" ", "_")

        if len(ext)>1:
            new_name = path+date+"."+ext[1]
            os.rename(path+fichier, new_name)

    elif "EXIF DateTimeOriginal" in tags.keys():
        ext = fichier.split(".")
        date = str(tags["EXIF DateTimeOriginal"]).replace(":", "_").replace(" ", "_")

        if len(ext)>1:
            new_name = path+date+"."+ext[1]
            os.rename(path+fichier, new_name)
    else:
        ext = fichier.split(".")
        date = str(datetime.fromtimestamp(os.stat(path+fichier).st_birthtime)).replace(":", "_").replace(" ", "_")

        if len(ext)>1:
            new_name = path+date+"."+ext[1]
            os.rename(path+fichier, new_name)

def grouper_par_an(path,  fichiers):
    nom_rep = ["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
    #nom_rep = []
    for f in fichiers:
        an = f.split("_")[0]
        #print(an)
        if an not in nom_rep:
            os.mkdir(path+an)
            #print(path+f, path+an+"/"+f)
            nom_rep.append(an)
            os.rename(path+f, path+an+"/"+f)
        else:
            #print(path + f, path + an + "/" + f)
            os.rename(path+f, path+an+"/"+f)

def conversion_to_jpg(path, fichier):
    image = PIL.Image.open(path+fichier)
    if not image.mode == 'RGB':
        image = image.convert('RGB')
    ext = fichier.split(".")
    if len(ext)>1:
        new_name = path+ext[0]+".jpg"
        image.save(new_name)
