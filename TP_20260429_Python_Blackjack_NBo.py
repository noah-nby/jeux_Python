"""Description globale.

# #############################################################################
# ## Objet : Blackjack
# ##
# ## Auteur : BOULAY Noah
# ## Date : 29 avril 2026
# ## Normalisation : PEP 8
# ## Nom du programme : TP_20260429_Python_Blackjack_NBo.py
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


if __name__ == "__main__":
    
    victoire = 0
    defaite = 0
    match_nul = 0
    #Initialisation.
    
    jouer_encore = input("Voulez-vous jouer ? (oui/non) : ")#Demande au joueur si il veut jouer.
    if jouer_encore == "oui":
        continuer_jeu = 1
    else:
        continuer_jeu = 0
        
    while continuer_jeu:
        carte_joueur = 0
        carte_bot = 0
        prise_carte = 0
        #Initialisation des variables de la partie du jeu.
        
        while prise_carte == 0 : #Boucle de la partie.
            choix_bot = random.randint(0, 1)
            choix_joueur = input("Voulez vous prendre une carte ? (oui/non) : ")
            print("------------------------")
            
            if choix_joueur == "oui": #Condition si le joueur prends une carte ou non.
                carte_joueur = carte_joueur + random.randint(1, 10)
            elif choix_joueur == "non":
                prise_carte = 1
                
            if choix_bot == 1: #Condition qui montre si le bot prends une carte ou non.
                carte_bot = carte_bot + random.randint(1, 10)
                print("Le bot prends une carte.")
                print("------------------------")
            else:
                print("Le bot ne prends pas de carte.")
                print("------------------------")
            
        if carte_joueur > 21: 
            print("Vous avez perdu !")
            print("------------------------")
            defaite = defaite + 1
        else:
            if carte_bot > 21:
                print("Vous avez gagnez !")
                print("------------------------")
                victoire = victoire + 1
            else:
                if carte_joueur < carte_bot:
                    print("Vous avez perdu !")
                    print("------------------------")
                    defaite = defaite + 1
                
                else:
                    if carte_joueur > carte_bot:
                        print("Vous avez gagnez !")
                        print("------------------------")
                        victoire = victoire + 1
                    
                    else:
                        print("Il y a match nul !")
                        print("------------------------")
                        match_nul = match_nul + 1
        #Vérification de chaque possibilité de fin de partie.
        
        print("Vos score sont, victoire :", victoire, ",défaite :", defaite, ",match nul :", match_nul)
        #Afficher les scores du joueur.
        
        rejouer = input("Voulez-vous quitter le programme ? (FIN/Fin/fin) : ").lower().strip()
        continuer_jeu = (rejouer != "fin")
        #Propose au joueur d'arrêter de jouer.
    
    print("Fin du jeu")
















































