"""Description globale.

# #############################################################################
# ## Objet : Création du jeu du pendu en Python
# ## Auteur : BOULAY Noah
# ## Date : 27 mars 2026
# ## Normalisation : PEP 8
# ## Nom du programme : 202602703_LePendu_NBo.py
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

def mettre_a_jour_affichage(mot_choisi, lettres_devinees):
    """
    Mettre à jour affichage.

    Parameters
    ----------
    mot_choisi : string
        C'est le mot aléatoire choisi.
    lettres_devinees : list
        Ce sont les lettres trouvées par le joueur.

    Returns
    -------
    affichage : string
        Affiche le mot avec les lettres qui sont trouvées.

    """
    affichage = ""
    for lettre in mot_choisi:
        if lettre in lettres_devinees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    return affichage

if __name__ == "__main__":
    mot = ["python", "programmation", "ordinateur", "informatique","algorithme",
           "serveur", "logiciel","navigateur", "developpeur", "cybersecurite", 
           "donnees", "javascript", "virtualisation","numerisation", "cryptographie",
           "developpement", "stockage", "connectivite", "multimedia","configuration",
           "optimisation", "authentification", "interoperabilite", "administrateur",
           "compilation", "deploiement", "systeme", "interface", "souris", "clavier"]
    #Ceci est la liste de mot pour le pendu.
    victoire = 0
    defaite = 0 
    partie_joue = 0
    
    jouer_encore = input("Voulez-vous jouer ? (oui/non) : ")
    if jouer_encore == "oui":
        continuer_jeu = 1
    else:
        continuer_jeu = 0
        #Demande au joueur si il veut jouer.

    while continuer_jeu:
        mot_choisi = random.choice(mot)
        lettres_devinees = [mot_choisi[0], mot_choisi[-1]]
        mauvaise_lettre = ""
        affichage = mettre_a_jour_affichage(mot_choisi, lettres_devinees)
        coups = 11
        #Initialisation de variable.

        while coups > 0:
            print("-----------------------------------------------------------------")
            print(affichage)
            print("Nombre de coups =", coups, "/", "mauvaise lettre =", mauvaise_lettre)
            choix_lettre = input("Choisir une lettre : ") 
            if choix_lettre in mot_choisi:
                lettres_devinees.append(choix_lettre)
                affichage = mettre_a_jour_affichage(mot_choisi, lettres_devinees)
            else:
                coups = coups - 1
                mauvaise_lettre += choix_lettre + " "
            #Déroulement de la partie, demande au joueur une lettre est la vérifie.

            if all(lettre in lettres_devinees for lettre in mot_choisi):
                print("-----------------------------------------------------------------")
                print(affichage)
                print("Vous avez gagné !")
                victoire = victoire + 1
                coups = -1
            #Vérifie si toutes les lettre du mots sont trouvé et dis au joueur qu'il a gagné.

        if coups == 0:
            print("-----------------------------------------------------------------")
            print("Vous avez perdu !")
            defaite = defaite + 1
        #Si le joueur n'a pas trouver toute les lettres du mot il a perdu.
        partie_joue = partie_joue + 1
        
        print("Vous avez joué :", partie_joue,", et vos victoires sont de", victoire, " et vos défaites de", defaite)

        rejouer = input("Voulez-vous quitter le programme ? (FIN/Fin/fin) : ").lower().strip()
        continuer_jeu = (rejouer != "fin")

    print("Fin du jeu")