"""Description globale.

# #############################################################################
# ## Objet : Jeu du morpion
# ##
# ## Auteur : BOULAY Noah
# ## Date : 7 avril 2026
# ## Normalisation : PEP 8
# ## Nom du programme : 20260407_leMorpion_NBo.py
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

def afficher_plateau():
    """
    Affiche le plateau.

    Returns
    -------
    None.

    """
    print(plateau[0], plateau[1], plateau[2])
    print(plateau[3], plateau[4], plateau[5])
    print(plateau[6], plateau[7], plateau[8])
    print("------")
    

def joueur_aleatoire():
    """
    Determine les 2 joueurs.

    Returns
    -------
    j1 : int
        Determine qui est le joueur 1 entre le bot et l'humain.
    j2 : int
        Determine qui est le joueur 2 entre le bot et l'humain.

    """
    choix_joueur = random.randint(0, 1)
    
    if choix_joueur == 1:
        j1 = 0 # Bot
        j2 = 1 # Humain
    else:    
        j1 = 1 # Humain
        j2 = 0 # Bot
        
    return j1, j2

def verification_victoire_j1():
    """
    Verifier chaque combinaison de victoire.

    Returns
    -------
    int
        Permet d'analyser si le joueur 1 gagne.

    """
    #ligne
    if carre_magique_j1[0] == 0 and carre_magique_j1[1] == 0 and carre_magique_j1[2] == 0:   
        return 1
    if carre_magique_j1[3] == 0 and carre_magique_j1[4] == 0 and carre_magique_j1[5] == 0:   
        return 1    
    if carre_magique_j1[6] == 0 and carre_magique_j1[7] == 0 and carre_magique_j1[8] == 0:   
        return 1
    #colonne    
    if carre_magique_j1[0] == 0 and carre_magique_j1[3] == 0 and carre_magique_j1[6] == 0:   
        return 1
    if carre_magique_j1[1] == 0 and carre_magique_j1[4] == 0 and carre_magique_j1[7] == 0:   
        return 1    
    if carre_magique_j1[2] == 0 and carre_magique_j1[5] == 0 and carre_magique_j1[8] == 0:   
        return 1
    #diagonale    
    if carre_magique_j1[0] == 0 and carre_magique_j1[4] == 0 and carre_magique_j1[8] == 0:   
        return 1    
    if carre_magique_j1[2] == 0 and carre_magique_j1[4] == 0 and carre_magique_j1[6] == 0:   
        return 1
    return 0    

def verification_victoire_j2():
    """
    Verifier chaque combinaison de victoire.

    Returns
    -------
    int
        Permet d'analyser si le joueur 2 gagne.

    """
    #ligne
    if carre_magique_j2[0] == 0 and carre_magique_j2[1] == 0 and carre_magique_j2[2] == 0:   
        return 1
    if carre_magique_j2[3] == 0 and carre_magique_j2[4] == 0 and carre_magique_j2[5] == 0:   
        return 1    
    if carre_magique_j2[6] == 0 and carre_magique_j2[7] == 0 and carre_magique_j2[8] == 0:   
        return 1
    #colonne    
    if carre_magique_j2[0] == 0 and carre_magique_j2[3] == 0 and carre_magique_j2[6] == 0:   
        return 1
    if carre_magique_j2[1] == 0 and carre_magique_j2[4] == 0 and carre_magique_j2[7] == 0:   
        return 1    
    if carre_magique_j2[2] == 0 and carre_magique_j2[5] == 0 and carre_magique_j2[8] == 0:   
        return 1
    #diagonale    
    if carre_magique_j2[0] == 0 and carre_magique_j2[4] == 0 and carre_magique_j2[8] == 0:   
        return 1    
    if carre_magique_j2[2] == 0 and carre_magique_j2[4] == 0 and carre_magique_j2[6] == 0:   
        return 1
    return 0

def verification_match_nul():
    """
    Vérifier chaque combinaison de match nul.

    Returns
    -------
    int
        Permet de vérifié si il y a un match nul.

    """
    if (plateau[0] == 'O' or plateau[0] == 'X') and \
    (plateau[1] == 'O' or plateau[1] == 'X') and \
    (plateau[2] == 'O' or plateau[2] == 'X') and \
    (plateau[3] == 'O' or plateau[3] == 'X') and \
    (plateau[4] == 'O' or plateau[4] == 'X') and \
    (plateau[5] == 'O' or plateau[5] == 'X') and \
    (plateau[6] == 'O' or plateau[6] == 'X') and \
    (plateau[7] == 'O' or plateau[7] == 'X') and \
    (plateau[8] == 'O' or plateau[8] == 'X'):
        return 1
    return 0
    
    
if __name__ == "__main__":

    
    jouer_encore = input("Voulez-vous jouer ? (oui/non) : ")#Demande au joueur si il veut jouer
    if jouer_encore == "oui":
        continuer_jeu = 1
    else:
        continuer_jeu = 0
    
    
    score_bot = 0
    score_humain = 0
    
    while continuer_jeu:             #Boucle de jeu
        j1, j2 = joueur_aleatoire()  #Choix aléatoire entre le bot et l'humain pour j1 et j2
        
        carre_magique_j1 = [2, 7, 6,
                            9, 5, 1,
                            4, 3, 8]
        
        carre_magique_j2 = [2, 7, 6,
                            9, 5, 1,
                            4, 3, 8]
        
        plateau = [1, 2, 3,
                   4, 5, 6, 
                   7, 8, 9]
        
        gagnant = 0
        match_nul = verification_match_nul()
        jeu = 0
        
        
        while gagnant == 0 and match_nul == 0:  #Boucle tant qu'il n'y a pas de gagnant ou de match nul.
            afficher_plateau()
            
            while jeu == 0:#Boucle du j1 qui place sont O
                if j1 == 0:   
                    case = random.randint(1, 9)
                    
                    if plateau[case - 1] == 'O' or plateau[case - 1] == 'X': #Vérifie si la case n'est pas prise.
                       print("Case déjà prise !")
                    else:
                       plateau[case - 1] = 'O'
                       carre_magique_j1[case - 1] = 0
                       jeu = 1
                       #Mets le 0 a la case choisi.
                       
                else:
                    case = int(input("J1 joue, choisissez une case entre 1 et 9 : "))
                    
                    if plateau[case - 1] == 'O' or plateau[case - 1] == 'X': #Vérifie si la case n'est pas prise.
                       print("Case déjà prise !")
                    else:
                       plateau[case - 1] = 'O'
                       carre_magique_j1[case - 1] = 0
                       jeu = 1
                       #Mets le 0 a la case choisi.
                       
            match_nul = verification_match_nul()
            if match_nul == 1:
                jeu = 0
            #Vérification de match nul.
            afficher_plateau()       
            gagnant = verification_victoire_j1()
            
            while jeu == 1: #Boucle du j2 qui place X.
                if j2 == 0:   
                    case = random.randint(1, 9)
                    
                    if plateau[case - 1] == 'O' or plateau[case - 1] == 'X': #Vérifie si la case n'est pas prise.
                       print("Case déjà prise !")
                    else:
                       plateau[case - 1] = 'X'
                       carre_magique_j2[case - 1] = 0
                       jeu = 0
                       #Mets le X a la case choisi.
                       
                else:
                    case = int(input("J2 joue, choisissez une case entre 1 et 9 : "))
                    
                    if plateau[case - 1] == 'O' or plateau[case - 1] == 'X': #Vérifie si la case n'est pas prise.
                       print("Case déjà prise !")
                    else:
                       plateau[case - 1] = 'X'
                       carre_magique_j2[case - 1] = 0
                       jeu = 0
                       #Mets le X a la case choisi.
               
            if gagnant == 0:
               gagnant = verification_victoire_j2()
             
        if verification_victoire_j1() == 1:
            if j1 == 1:  
                score_humain = score_humain + 1
            else:      
                score_bot = score_bot + 1
        
        if verification_victoire_j2() == 1:
            if j2 == 1:  
                score_humain = score_humain + 1
            else:        
                score_bot = score_bot + 1
        #On vérifie qui a gagné la partie entre le bot et le joueur.
            
        print("----------------------------")
        if match_nul == 1: #Vérifie si il y a un match nul.
            print("Le match est terminé, il y a eu match nul !")
        else:
            print("Le match est terminé !")
        afficher_plateau()
        print("Les scores sont bot :", score_bot, "humain :", score_humain)
        #Affiche les scores.
        
        rejouer = input("Voulez-vous quitter le programme ? (FIN/Fin/fin) : ").lower().strip()
        continuer_jeu = rejouer != "fin"
        #Demande si le joueur veut rejouer.
            
    print("Fin de jeu")        
        
        
        
        