"""Description globale.

# #############################################################################
# ## Objet : Tri a bulle
# ##
# ## Auteur : BOULAY Noah
# ## Date : 26 avril 2026
# ## Normalisation : PEP 8
# ## Nom du programme : 20260426_Python_Tri_Bulle_NBo.py
# #############################################################################
# ## Modification :
# ## Auteur :
# ## Date :
# #############################################################################
"""
#pylint: disable = W0311
#pylint: disable = C0303
#pylint: disable = C0103

import random

def creation_liste(a):
    """
    Création d'un liste de nombre.

    Parameters
    ----------
    a : int
        C'est le nombre de nombres dans la liste.

    Returns
    -------
    None.

    """
    global liste_nbr
    liste_nbr = [random.randint(0, 1000) for i in range(a)]

if __name__ == "__main__":
    
    
    jouer_encore = input("Voulez-vous jouer ? (oui/non) : ")
    if jouer_encore == "oui":
        continuer_jeu = 1
    else:
        continuer_jeu = 0
    #Demande si le joueur veut jouer.
        
    while continuer_jeu:
        taille_liste = 50
        creation_liste(taille_liste)
        #Initialisation de la liste aléatoire.
        print("Voici la liste qui va être trié :", 
              liste_nbr)
        #Affiche la liste non trié.
        tri = 1 
        while tri == 1:
            tri = 0
            for i in range(taille_liste-1):
                if liste_nbr[i] > liste_nbr[i+1]:
                    liste_nbr[i], liste_nbr[i+1] = liste_nbr[i+1], liste_nbr[i]
                    tri = 1
                    print(liste_nbr)
                    #Le tri de la liste.
        
        
        print("Le tri est terminé la liste triée ressemble à :", liste_nbr)
        #Affiche la liste trié.
        
        rejouer = input("Voulez-vous quitter le programme ?(FIN/Fin/fin): ").lower().strip()
        continuer_jeu = (rejouer != "fin")
        #Demande au joueur si il veut quitter le programme.
    
    print("Fin du jeu")
        
        
