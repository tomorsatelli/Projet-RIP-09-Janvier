class Routeur:
    def __init__(self, nom):
        # Initialise le routeur avec un nom, une table de routage et une liste de voisins vides.
        self.nom = nom
        self.table = []  # Table de routage : [destination, passerelle, distance]
        self.voisin = []  # Liste des voisins directs
    
    def ajoute_voisin(self, routeur):
        # Ajoute un voisin à la liste des voisins.
        self.voisin.append(routeur)
    
    def affiche_table(self):
        # Affiche la table de routage.
        print(f"\nTable de routage pour {self.nom}:")
        print("+---------------+---------------+----------+")
        print("| Destination   | Passerelle    | Distance |")
        print("+---------------+---------------+----------+")
        for entree in self.table:
            print(f"| {entree[0]:<13} | {entree[1]:<13} | {entree[2]:<8} |")
        print("+---------------+---------------+----------+")
    
    def affiche_voisins(self):
        # Affiche les noms des voisins directs.
        print(f"\nNoms des voisins directs de {self.nom}:")
        for voisin in self.voisin:
            print(f"- {voisin.nom}")
    
    def mise_a_jour(self, table_voisin):
        # Met à jour la table de routage à partir de la table d'un voisin.
        for entree in table_voisin:
            destination, passerelle, distance = entree
            distance += 1  # Ajoute 1 à la distance pour tenir compte du passage par le voisin
            trouve = False
            for i, existante in enumerate(self.table):
                if existante[0] == destination:
                    trouve = True
                    if distance < existante[2]:  # Met à jour si la nouvelle distance est plus courte
                        self.table[i] = [destination, passerelle, distance]
                    break
            if not trouve:
                # Ajoute une nouvelle entrée si la destination est absente.
                self.table.append([destination, passerelle, distance])
