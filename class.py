class Routeur:
    def __init__(self, nom):
        self.nom = nom
        self.table = []  # Table de routage
        self.voisin = []  # Liste des voisins
    
    def ajoute_voisin(self, routeur):
        self.voisin.append(routeur)
    
    def affiche_table(self):
        print(f"\nTable de routage pour {self.nom}:")
        print("+---------------+---------------+----------+")
        print("| Destination   | Passerelle    | Distance |")
        print("+---------------+---------------+----------+")
        for entree in self.table:
            print(f"| {entree[0]:<13} | {entree[1]:<13} | {entree[2]:<8} |")
        print("+---------------+---------------+----------+")
    
    def affiche_voisins(self):
        print(f"\nNoms des voisins directs de {self.nom}:")
        for voisin in self.voisin:
            print(f"- {voisin.nom}")
    
    def mise_a_jour(self, table_voisin):
        for entree in table_voisin:
            destination, passerelle, distance = entree
            distance += 1  # La distance est augmentée de 1 en raison du passage par le voisin
            trouve = False
            for i, existante in enumerate(self.table):
                if existante[0] == destination:
                    trouve = True
                    if distance < existante[2]:
                        self.table[i] = [destination, passerelle, distance]
                    break
            if not trouve:
                self.table.append([destination, passerelle, distance])