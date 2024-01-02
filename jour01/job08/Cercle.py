from math import *

class Cercle:
    
    def __init__(self,rayon):
        self.rayon = rayon
    
    def changerRayon(self,nr):
        self.rayon = nr
    
    def circonférence(self):
        return 2 * pi * self.rayon

    def aire(self):
        return (self.rayon ** 2) * pi

    def diametre(self):
        return self.rayon * 2
    
    def afficherInfos(self):
        print(f"Le cercle a un rayon de {self.rayon}")
        print(f"Le cercle a un diametre de {self.diametre()}")
        print(f"Le cercle a une circonference de {self.circonférence()}")
        print(f"Le cercle a une aire de {self.aire()}")