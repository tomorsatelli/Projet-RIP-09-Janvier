import time

def pasapas(reseau):
    print("\n=== Routeurs disponibles ===")
    for nom in reseau.keys():
        print(f"- {nom}")

    nom_routeur = input("\nEntrez le nom d'un routeur (ou 'exit' pour quitter) : ").strip()
    if nom_routeur.lower() == 'exit':
        print("Fin du contrôle pas à pas.")
        return

    if nom_routeur not in reseau:
        print(f"Le routeur '{nom_routeur}' n'existe pas dans le réseau.")
        return

    routeur = reseau[nom_routeur]
    print(f"\nTable de routage avant propagation pour {nom_routeur}:")
    routeur.affiche_table()

    # Propager la table de routage à tous les voisins
    print(f"\nPropagation de la table de routage de {nom_routeur} :")
    for voisin in routeur.voisin:
        print(f"- Mise à jour de la table de routage de {voisin.nom}")
        voisin.mise_a_jour(routeur.table)

    # Afficher les tables de routage mises à jour
    print("\n=== Tables de routage mises à jour ===")
    for nom, routeur in reseau.items():
        print(f"\nTable de routage pour {nom}:")
        routeur.affiche_table()

def deterministe(reseau):
    convergence = False
    while not convergence:
        convergence = True  # On suppose que les tables ont convergé
        print("\n=== Mise à jour des tables de routage ===")
        
        for routeur in reseau.values():
            # Afficher la table avant la propagation
            print(f"\nTable de routage avant propagation pour {routeur.nom}:")
            routeur.affiche_table()

            # Sauvegarder l'état initial de la table de routage pour vérifier la convergence
            table_initiale = [entree[:2] for entree in routeur.table]  # On garde seulement Destination et Passerelle
            
            # Propager la table de routage de chaque routeur à ses voisins
            print(f"\nPropagation de la table de routage de {routeur.nom} :")
            for voisin in routeur.voisin:
                print(f"- Mise à jour de la table de routage de {voisin.nom}")
                voisin.mise_a_jour(routeur.table)

            # Vérifier si la table a changé
            for entree_initiale, entree_nouvelle in zip(table_initiale, [entree[:2] for entree in routeur.table]):
                if entree_initiale != entree_nouvelle:
                    convergence = False  # Les tables n'ont pas convergé si un changement a eu lieu

            # Attendre 2 secondes avant de propager à nouveau
            time.sleep(2)
        
        print("\nLes tables de routage ont convergé.")
