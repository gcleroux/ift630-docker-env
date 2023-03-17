// kernel.cl
//-----------
// Noyau openCL calculant la convolution pour un certain nombre de points
// d'une image
//
// Entrée : image : l'image à traiter (emmagasinée dans un tableau 1D)
//          taille : taille de la partie de l'image à traiter (en 1D)
//          filtre : le filtre à appliquer sur l'image
//          taille_filtre : la dimension du filtre
//          tx : la dimension en «x» de l'image (nb lignes)
//          ty : la taille en «y» de l'image  (nb colonnes) 
// Sortie  : sortie : image modifiée
//
__kernel void convo( __global char* sortie, __global const char * image, int taille, double filtre, int taille_filtre, int tx, int ty)
{
    int index = get_global_id(0);        // on obtient l'identificateur du fil d'exécution
    unsigned int dis = taille_filtre/2;  // on calcule la distance à traiter autour du pixel
    float res;                           // pour accumuler le pixel résultant
    //----------------------------------------------------------------------
    // Chaque fil (noyau) traite une partie de l'image de taille «taille».  
    // Selon l'index du fil on détermine quelle partie le fil doit traiter
    int debut = taille*index;            // on détermine où débute le traitement de l'image
    int fin1 = debut + taille -1 ;       // on détermine où se termine le traitement de l'image
    //-----------------------------------------------------------------------
    // **** Possible impression l'intérieur du noyau (pour mise au point) ***
    //if (index == 1) printf(" Fil %d, debut = %d, fin = %d, (%d:%d), (%d,%d)\n", index, debut, fin1, debut/ty, debut%tx,fin1/ty,fin1%tx );
    //----------------------------------------------------------------------
    // On parcourt l'image pour traiter chaque pixel
    for (int indice = debut; indice <= fin1 ;indice++)
    {   
        // L'image est emmagasinée dans un tableau 1D.
        // Selon la taille de l'image on se repositionne en 2D (ligne et colonne)
        int ligne = indice/ty; 
        int col = indice%tx;
        res=0.0;
        //-------------------------------------------------------------------
        //On applique le filtre sur le pixel
        for (int i = 0 ; i < taille_filtre; i++)
        {
            for (int j = 0; j < taille_filtre; j++)
            {
                // calcul des indices pour appliquer le filtre
                int indice1 = ligne - dis + i;   //indice pour la ligne
                int indice2 = col - dis + j ;    // indice pour la colonne
                if (indice1 < 0) indice1 = 0;    // au cas où l'indice soit à l'extérieur de l'image
                if (indice2 < 0 ) indice2 = 0;   // au cas où l'indice soit à l'extérieur de l'image
                if (indice1 > tx-1) indice1 = tx-1;  // au cas où l'indice soit à l'extérieur de l'image
                if (indice2 > ty-1) indice2 = ty-1; // au cas où l'indice soit à l'extérieur de l'image
                // on applique le filtre et cumule le résultat
                res += (unsigned char)(image[indice1*tx + indice2]) * filtre;
                //-----------------------------------------------------------------------
                // **** Possible impression l'intérieur du noyau (pour mise au point) ***
                //if (index == 1 && test==1) printf("image[%d,%d], %d, %d, %f, %d\n", ligne, col, indice1, indice2, res , (unsigned char) res);
            }
        }
        sortie[ligne*ty + col]= (unsigned char)(res);   // on sauve le nouveau pixel dans l'image de sortie
        //-------------------------------------------------------------------
        // **** Possible impression l'intérieur du noyau (pour mise au point) ***
        //if (index == 1) printf("image[%d,%d](%d)= %d, ", ligne, col, ligne*ty + col, (unsigned char)res );
    }
}

