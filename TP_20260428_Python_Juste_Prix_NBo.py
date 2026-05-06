"""Description globale.

# #############################################################################
# ## Objet : Juste prix
# ##
# ## Auteur : BOULAY Noah
# ## Date : 28 avril 2026
# ## Normalisation : PEP 8
# ## Nom du programme : TP_20260428_Python_Juste_Prix_NBo.py
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
    
    
    jouer_encore = input("Voulez-vous jouer ? (oui/non) : ")
    if jouer_encore == "oui":
        continuer_jeu = 1
    else:
        continuer_jeu = 0
    #Demande au joueur si il veut jouer.
        
    while continuer_jeu:
        vie = 10
        chiffre_secret = random.randint(0, 1000)
        print("Vous êtes dans le jeu du juste prix !")
        chiffre_choisi = []
        #Initialisation du jeu.
        
        while vie > 0:
            try:
                print("_______________________")
                print("Vous avez", vie, "de vie")
                print(chiffre_choisi)
                choix_chiffre = int(input("Choisissez un nombre entre 0 et 1000 : "))
                
                if choix_chiffre == chiffre_secret:
                    print("_______________________")
                    print("Vous avez trouvé le chiffre secret : ", chiffre_secret)
                    vie = -1
                else:
                    if choix_chiffre > chiffre_secret:
                        print("_______________________")
                        print("Le chiffre est trop grand ! : ", choix_chiffre)
                        vie = vie - 1
                        chiffre_choisi.append(choix_chiffre)
                    else:
                        if choix_chiffre < chiffre_secret:
                            print("_______________________")
                            print("Le chiffre choisi est trop petit ! : ", choix_chiffre)
                            vie = vie - 1
                            chiffre_choisi.append(choix_chiffre)
                        else:
                            print("_______________________")
                            print("Il y a une erreur dans le choix du nombre")
                #Déroulement de la partie avec vérification du chiffre choisi du joueur.
            except ValueError as e:
                print("_______________________")
                print(f"Erreur {e}")
                #Affiche si il y a une erreur de saisi.
        
        
        
        print("_______________________")    
        print("La partie est terminée !")
        if vie == 0:
            print("Vous avez perdu la partie !")
            print("Le chiffre était :", chiffre_secret)
            defaite = defaite + 1
        else:
            print("Vous avez gagné la partie !")
            victoire = victoire + 1
             
        print("Vos victoires sont de :", victoire, ",et vos défaites sont de :", defaite)
        #Affiche si le joueur a gagné ou perdu et son score.
        
        rejouer = input("Voulez-vous arrêter ? (FIN/Fin/fin) : ").lower().strip()
        continuer_jeu = (rejouer != "fin")
        #Demande au joueur si il veut quitter le programme.

    print("Fin du jeu")























    

