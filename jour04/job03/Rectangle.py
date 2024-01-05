class Rectangle:
    def __init__(self,longeur,largeur):
        self.__longeur = longeur
        self.__largeur = largeur
    
    def get_longeur(self):
        return self.__longeur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longeur(self,longeur):
        self.__longeur = longeur
    
    def set_largeur(self,largeur):
        self.__largeur = largeur
    
    def perimètre(self):
        print(f"Le perimetre du rectange est : {2*self.__longeur + 2*self.__largeur}")
        
    def surface(self):
        print(f"La surface du rectange est : {self.__longeur * self.__largeur}")