//  ConvolutionMT1.cpp
//-------------------
// Ce programme implante un calcul de convolution sur une image en utilisant les fils d'exécution
// Le filtre utilisé est un filtre moyenneur.
// Le programme ne fonctionne que sur des images de type «raw»
//
// Paramètres sur la lignre de commandes
//  - Parm #1 : nombre de fils à utiliser
//  - Parm #2 : taille «horizontale» de l'image 
//  - Parm #3 : taille «verticale» de l'image 
//  - Parm #4 : nom du fichier contenant l'image
//  - Parm #5 : nom du fichier de sortie
//  - Parm #6 : taille du filtre

#include <thread>
#include <sstream>
#include <iostream>
#include <fstream>
#include <chrono>
#include <vector>

using namespace std;
using namespace std::chrono;

// Fonction convolution
// Cette fonction calcule la convolution pour un certain nombre de points
// d'une image
//
// Entrée : index - identificateur du fil 
//          taille : taille de la partie de l'image à traiter (en 1D)
//          filtre : le filtre à appliquer sur l'image
//          taille_filtre : la dimension du filtre
//          image : l'image à traiter (emmagasinée dans un tableau 1D)
//          tx : la dimension en «x» de l'image (nb lignes)
//          ty : la taille en «y» de l'image  (nb colonnes) 
// Sortie  : sortie : image modifiée
//
void convolution(int index, int taille, double filtre, uint8_t taille_filtre, const char* image, int tx, int ty, uint8_t* sortie)
{
    uint8_t dis = taille_filtre/2;  // on calcule la distance à traiter autour du pixel
    double res;                     // pour accumuler le pixel résultant
    //----------------------------------------------------------------------
    // Chaque fil (noyau) traite une partie de l'image de taille «taille».  
    // Selon l'index du fil on détermine quelle partie le fil doit traiter   
    int debut = taille*index;
    int fin1 = debut + taille -1 ;
    //---------------------------------------------------------------------
    // *** Possible impression pour mise au point ****
    // cout << "Fil" << index << " debute a " << debut << " jusqu'a " << fin1 << " --> " 
    //      << debut%ty <<","<< debut%tx << " -- " <<fin1/ty<<","<<fin1/tx<< endl;
    // cout << taille_filtre << "  -- " << dis << " -- " << tx << " -- " << ty << endl;
    //-------------------------------------------------------------------------
    // On parcourt l'image pour traiter chaque pixel
    for (int indice = debut; indice <= fin1 ; indice ++)
    {
        // L'image est emmagasinée dans un tableau 1D.
        // Selon la taille de l'image on se repositionne en 2D (ligne et colonne)
        int ligne = indice/ty; 
        int col = indice%tx;
        res=0.0;
        //-------------------------------------------------------------------
        // Application du filtre sur le pixel
        for (int i = 0 ; i < taille_filtre; i++)
        {
            for (int j = 0; j < taille_filtre; j++)
            {
                // calcul des indices pour appliquer le filtre
                int indice1 = ligne - dis + i;   //indice pour la ligne
                int indice2 = col - dis + j ;    // indice pour la colonne
                if (indice1 < 0) indice1 = 0;    // au cas où l'indice soit à l'extérieur de l'image
                if (indice2 < 0) indice2 = 0;    // au cas où l'indice soit à l'extérieur de l'image
                if (indice1 > tx-1) indice1 = tx-1;  // au cas où l'indice soit à l'extérieur de l'image
                if (indice2 > ty-1) indice2 = ty-1;  // au cas où l'indice soit à l'extérieur de l'image
                // on applique le filtre et cumule le résultat
                res += uint8_t(image[indice1*tx + indice2]) * filtre;
                //---------------------------------------------------------------------
                // *** Possible impression pour mise au point ****
                //cout << "Resultats = " << indice1 << " - " << indice2 
                //     << " pixel " << int(image[indice1*tx + indice2]) << " --> " <<  int(res) << endl;
            }
        }
        sortie[ligne*tx + col]= uint8_t(res);
     }
}
/*********************************************************************
   Programme pincipal qui prépare le calcul et le lance
 **********************************************************************/
                 
int main(int argc, char *argv[])
{
    int taille_filtre;
    int th_image, tv_image;
    int nbFils;
    ifstream image;
    ofstream image_res;
    string nom,nom_sortie,tmp;
    const char* texte =0; 
    
    // Récupération des paramètres
    nbFils = stoi(argv[1]);
    th_image = stoi(argv[2]);
    tv_image = stoi(argv[3]);
    nom = argv[4];
    nom_sortie = argv[5];
    taille_filtre = (uint8_t)stoi(argv[6]);
    //---------------------------------------------------------------
    // Lecture de l'image dans un tableau de caratères (à une dimension)
    image.open(nom);         // ouverture du fichier
    if (image.is_open())
    {
      ostringstream ss;      // on veut lire dans une stream
      ss << image.rdbuf();   // lecture de tout le fichier (fichier raw seulement)
      tmp = ss.str();        // on convertit en string
      texte = tmp.c_str();   // on place l'image dans une chaine de caractères
      image.close();
    }
    else 
	{
		cout << "Impossible d'ouvrir le fichier"; 
		return -1;
	}
	
    int taille_texte = tmp.size();  // récupération de la taille de l'aimge (en 1D)
    // ------
    /// À des fins de mise au point
    // cout << "taille du texte = " << taille_texte << endl;
    // ------
    // On alloue le tableau pour l'image de sortie
    uint8_t* sortie = new uint8_t[taille_texte];  
    //-------
    // On calcule le filtre moyenneur
    double valeur = 1.0/ (taille_filtre * taille_filtre);
    //-------
    // On détermine la dimension de l'image à traiter par chaque fil (ou coeurs)
    // le dernier fil traite aussi les pixels «restant»
    int temp, temp2;
    temp = taille_texte / nbFils;
    temp2 = temp + (taille_texte % nbFils);
    
    // -----
    // On positionne le chronomètre pour évaluer la performance
    auto temps_depart = system_clock::now();
    // Pour se souvenir des fils.........
    vector<thread> threads;
    // Démarrage des fils 
    for (int i = 0; i< nbFils; i++)
    {  
         if (i != nbFils-1) threads.push_back(thread(convolution,i, temp, valeur, taille_filtre, texte, th_image, tv_image, sortie));
         else threads.push_back(thread(convolution,i, temp2, valeur, taille_filtre, texte, th_image, tv_image, sortie));
    } 
    // Attente de la fin d'exécution de tous les fils
    for(auto& thread : threads)
    {  thread.join(); }
    
    //===============================================
    // Arrêt du chronomètre
    auto temps_arret = system_clock::now();
    //----------------
    // Sauvegarde du résultat dans un fichier 
    image_res.open(nom_sortie,ios::binary | ios::out);
    if (image_res.is_open())
    {
      for (int ind=0; ind < taille_texte; ind++)
          image_res << sortie[ind];
      image_res.close();
    }
    else cout << "Impossible d'ouvrir le fichier"; 
    // ----------------
    // Affichage du temps d'exécution
    auto duree = duration_cast<milliseconds>(temps_arret - temps_depart);
    cout << "Temps execution = " << duree.count()/1000.0 << " secondes" << endl;
    return 0;
}
