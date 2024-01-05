from Vehicule import Vehicule

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roue : {self.roue}")
    
    def demarrer(self):
        print("La moto roule")