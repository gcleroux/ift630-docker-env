#!/usr/bin/env python
#  Convolution.py
#-------------------
# Ce programme implante un calcul de convolution sur une image en utilisant les fils d'exécution
# Le filtre utilisé est un filtre moyenneur.
# Le programme ne fonctionne que sur des images de type «raw»
#
# Paramètres sur la lignre de commandes
#  - Parm #1 : nombre de fils à utiliser
#  - Parm #2 : taille «horizontale» de l'image 
#  - Parm #3 : taille «verticale» de l'image 
#  - Parm #4 : nom du fichier contenant l'image
#  - Parm #5 : nom du fichier de sortie
#  - Parm #6 : taille du filtre
import sys
import time
from threading import Thread
from datetime import datetime
import numpy as np
from ctypes import *
import struct

# Fonction convolution
# Cette fonction calcule la convolution pour un certain nombre de points
# d'une image
#
# Entrée : index - identificateur du fil 
#          taille : taille de la partie de l'image à traiter (en 1D)
#          filtre : le filtre à appliquer sur l'image
#          taille_filtre : la dimension du filtre
#          image : l'image à traiter (emmagasinée dans un tableau 1D)
#          tx : la dimension en «x» de l'image (nb lignes)
#          ty : la taille en «y» de l'image  (nb colonnes) 
# Sortie  : sortie : image modifiée
#
def convolution(index, taille, filtre, taille_filtre, image, tx, ty, sortie):
    
    dis = int(taille_filtre/2)   # on calcule la distance à traiter autour du pixel
    #----------------------------------------------------------------------
    # Chaque fil (noyau) traite une partie de l'image de taille «taille».  
    # Selon l'index du fil on détermine quelle partie le fil doit traiter   
    debut = int(taille*index)
    fin1 = int(debut + taille) 
    #----------
    # ****** impression pour mise au point ***************
    print("Fil", index, " debute a ", debut, " jusqu'a ", fin1-1, " --> " ,int(debut/tx),",",debut%tx , " -- ",int((fin1-1)/tx),",",(fin1-1)%tx)
    #-------------------------------------------------------------------------
    # On parcourt l'image pour traiter chaque pixel
    for indice  in range(debut,fin1):
        # L'image est emmagasinée dans un tableau 1D.
        # Selon la taille de l'image on se repositionne en 2D (ligne et colonne)
        ligne  = int(indice/ty)
        col = int(indice%tx)
        res=0.0;
        #-------------------------------------------------------------------
        # Application du filtre sur le pixel
        for i in range(0, taille_filtre):
             for j in range(0,taille_filtre):
                 indice1 = ligne - dis + i;         #indice pour la ligne
                 indice2 = col - dis + j ;          # indice pour la colonne
                 if indice1 < 0  : indice1 = 0      # au cas où l'indice soit à l'extérieur de l'image
                 if indice2 < 0  : indice2 = 0      # au cas où l'indice soit à l'extérieur de l'image
                 if indice1 > tx-1 : indice1 = tx-1     # au cas où l'indice soit à l'extérieur de l'image
                 if indice2 > ty-1 : indice2 = ty-1     # au cas où l'indice soit à l'extérieur de l'image
                 # Application du filtre et cumul du résultat
                 res += np.uint8(image[indice1*tx + indice2]) * filtre;
                 # ****** Possible impression pour mise au point
                 #print("Resultats = ", indice1, " - ", indice2, " pixel ", int(image[indice1*tx + indice2]), " --> ",  np.uint8(res))
        # sauvegarde du résultat dans l'image de sortie
        sortie[ligne*tx + col]= np.uint8(res)
        # ****** Possible impression pour mise au point
        #print("Resultats = ", ligne, " - ", col, " pixel ", int(image[ligne*tx + col]), " --> ",  np.uint8(res))

#*********************************************************************
#   Programme pincipal qui prépare le calcul et le lance
# **********************************************************************

if __name__=="__main__":

   # Récupération des paramètres
    nbFils = eval(sys.argv[1])
    th_image = eval(sys.argv[2])
    tv_image = eval(sys.argv[3])
    nom = str(sys.argv[4])
    nom_sortie = str(sys.argv[5])
    taille_filtre = eval(sys.argv[6])
  
   
   # Lecture de l'image
    f = open(nom, mode = "rb")
    texte = f.read()   
    taille_texte= len(texte) 
    print(taille_texte)    
    #---------
    # Création d'un tableau d'octets pour le fichier de sortie
    sortie = bytearray(taille_texte)

    # Calcul de la valeur du filtre moyenneur
    filtre = 1.0/ (taille_filtre * taille_filtre);
    #-------
    # On détermine la dimension de l'image à traiter par chaque fil (ou coeurs)
    # le dernier fil traite aussi les pixels «restant»
    temp = taille_texte / nbFils;
    temp2 = temp + (taille_texte % nbFils)
    # -----
    # Positionnement du chronomètre pour évaluer la performance
    debut = datetime.now()
    # ----
    # Démarrage des processus 
    threads = []
    for n in range(0, nbFils):
        if n < nbFils-1 : t = Thread(target=convolution, args=(n, temp, filtre, taille_filtre, texte, th_image, tv_image, sortie))
        else : t = Thread(target=convolution, args=(n, temp2, filtre, taille_filtre, texte, th_image, tv_image, sortie))
        threads.append(t)
        t.start()
    # Attente de la fin d'exécution des fils
    for t in threads: t.join()
    #===============================================
    # Arrêt du chronomètre
    fin = datetime.now()
    # Sauvegarde du résultat dans fichier de sortie
    f = open(nom_sortie, mode = "wb")
    f.write(sortie)
    #----------------
    # Affichage du temps d'exécution
    delta = fin -debut
    print("temps d'exécution en secondes = ", delta.total_seconds())
 

