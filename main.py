import time
from lesclass import Routeur
from fonctions import *






# Exemple d'utilisation
if __name__ == "__main__":
    # Création de trois routeurs
    routeur_A = Routeur("Routeur_A")
    routeur_B = Routeur("Routeur_B")
    routeur_C = Routeur("Routeur_C")

    # Ajout des voisins
    routeur_A.ajoute_voisin(routeur_B)
    routeur_B.ajoute_voisin(routeur_C)

    # Ajout des entrées initiales dans les tables de routage
    routeur_A.table.append(["Destination_X", "Routeur_A", 0])
    routeur_B.table.append(["Destination_Y", "Routeur_B", 0])
    routeur_C.table.append(["Destination_Z", "Routeur_C", 0])

    # Dictionnaire des routeurs pour l'interaction pas à pas
    reseau = {
        routeur_A.nom: routeur_A,
        routeur_B.nom: routeur_B,
        routeur_C.nom: routeur_C
    }
    pasapas(reseau)
    # Lancer la fonction déterministe
    deterministe(reseau)
