class Vehicule:
    def __init__(self,marque,modele,annee,prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        
    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modele : {self.modele}")
        print(f"Annee : {self.annee}")
        print(f"Prix : {self.prix}")
    
    def demarrer(self):
        print("Attention, je roule")