from Rectangle import Rectangle

class Parallelepipede(Rectangle):
    def __init__(self, longeur, largeur,hauteur):
        super().__init__(longeur, largeur)
        self.hauteur = hauteur
    
    def volume(self):
        print(f"Le volume du parallélépipède est de {self.__longeur * self.__largeur * self.hauteur}")
    