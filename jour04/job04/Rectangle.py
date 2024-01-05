from Forme import Forme

class Rectangle(Forme):
    def __init__(self,largeur,hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.hauteur * self.largeur
    
    