
// conviolutionCL.cpp
//-------------------
// Ce programme implante un calcul de convolution sur une image en utilisant la carte graphique (openCL)
// Le filtre utilisé est un filtre moyenneur.
// Le programme ne fonctionne que sur des images de type «raw»
//
// Paramètres sur la lignre de commandes
//  - Parm #1 : nombre de coeurs à utiliser
//  - Parm #2 : nombre de groupes à utiliser (mettre 0 généralement)
//  - Parm #3 : taille «horizontale» de l'image 
//  - Parm #4 : taille «verticale» de l'image 
//  - Parm #5 : nom du fichier contenant l'image
//  - Parm #6 : nom du fichier de sortie
//  - Parm #7 : taille du filtre

#include <stdlib.h>
#include <stdio.h>
#include <CL/cl.h>
#include <iostream>
#include "contexte.h"
#include "program.h"
#include <sstream>
#include <chrono>
 
using namespace std;
using namespace std::chrono;

int main(int argc, char *argv[])
{
    int taille_filtre;
    int th_image, tv_image;
    ifstream image;
    ofstream image_res;
    string nom, nom_sortie, tmp;
    const char* texte; 
    int nbCoeurs, nbGroupes;
    
    // Récupération des paramètres
    nbCoeurs = stoi(argv[1]);
    nbGroupes = stoi(argv[2]);
    th_image = stoi(argv[3]);
    tv_image = stoi(argv[4]);
    nom = argv[5];
    nom_sortie = argv[6];
    taille_filtre = stoi(argv[7]);
    //---------------------------------------------------------------
    // Lecture de l'image dans un tableau de caratères (à une dimension)
    image.open(nom);         // ouverture du fichier
    if (image.is_open())
    {
      ostringstream ss;      // on veut lire dans une stream
      ss << image.rdbuf();   // lecture de tout le fichier (fichier raw seulement)
      tmp = ss.str();        // on convertit en stribg
      texte = tmp.c_str();   // on place l'image dans une chaine de caractères
      image.close();
    }
    else cout << "Impossible d'ouvrir le fichier"; 
    int taille_texte = tmp.size();  // récupération de la taille de l'aimge (en 1D)
    // ------
    /// À des fins de mise au point
    // cout << "taille du texte = " << taille_texte << endl;
    // ------
    // On alloue le tableau pour l'image de sortie
    char * sortie = new char[taille_texte];  
    //-------
    // On calcule le filtre moyenneur
    double valeur = 1.0/ (taille_filtre * taille_filtre);
    //-------
    // On détermine la dimension de l'image à traiter par chaque fil (ou coeurs)
    // On ignore le reste si la taille de l'image ne se divise pas par le nombre de fils
    int temp;
    temp = taille_texte / nbCoeurs;           // Chacun traite un fraction de l'image
    // -----
    // On positionne le chronomètre pour évaluer la performance
     auto temps_depart = system_clock::now();
 
    //===============================================
    // Initialision et exécution du programme openCL
    Contexte mon_contexte;   // création du contexte d'exécution (type de carte)
    // Chargement, compilation et préparation du programme noyau
    Program mon_prog(mon_contexte, "./kernel.cl", "convo");
    // Initialisation des paramètres
    mon_prog.initPara(sortie,taille_texte, SORTIE);  // image de sortie
    mon_prog.initPara(texte, taille_texte, ENTREE);  // image en entrée
    mon_prog.initPara(temp);                         // taille de l'image à traiter
    mon_prog.initPara(valeur);                       // valeur du filtre
    mon_prog.initPara(taille_filtre);                // taille du filtre
    mon_prog.initPara(th_image);                     // taille en «x» de l'image
    mon_prog.initPara(tv_image);                     // taille en y de l'image
    // Exécution du programme
    mon_prog.execute(1, nbCoeurs,nbGroupes, sortie); 
    //===============================================
    // On arrête le chronomètre
    auto temps_arret = system_clock::now();
    //----------------
    // On sauve le résultat dans un fichier 
    image_res.open(nom_sortie,ios::binary | ios::out);
    if (image_res.is_open())
    {
      for (int ind=0; ind < taille_texte; ind++)
        image_res << sortie[ind];
      image_res.close();
    }
    else cout << "Impossible d'ouvrir le fichier"; 
    // ----------------
    // Affichage u temps d'exécution
    auto duree = duration_cast<milliseconds>(temps_arret - temps_depart);
    cout << "Temps execution = " << duree.count()/1000.0 << " secondes" << endl;
    return 0;
}
