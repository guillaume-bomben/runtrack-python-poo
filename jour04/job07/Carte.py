class Carte:
    def __init__(self,valeur,couleur):
        self.valeur = valeur
        self.couleur = couleur
        self.paquet = self.allCard()
    
    def allCard(self):
        paquet = {}
        for c in self.couleur:
            for v in self.valeur:
                if v != "valet" and v != "dame" and v != "roi":
                    paquet[f"{v} de {c}"] = int(v)
                else:
                    paquet[f"{v} de {c}"] = 10
        return paquet

    def ValCard(self,carte):
        return self.paquet.get(carte)