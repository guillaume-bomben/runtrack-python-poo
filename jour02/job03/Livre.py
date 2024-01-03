class Livre:
    def __init__(self,titre,auteur,nbpage,disponible=True):
        self.__Titre = titre
        self.__Auteur = auteur
        self.__NbPage = nbpage
        self.__Disponible = disponible
        
    def get_Titre(self):
        return self.__Titre
    
    def get_Auteur(self):
        return self.__Auteur
    
    def get_NbPage(self):
        return self.__NbPage
    
    def set_Titre(self,titre):
        self.__Titre = titre
    
    def set_Auteur(self,auteur):
        self.__Auteur = auteur
    
    def set_NbPage(self,nbpage):
        if nbpage > 0 and type(nbpage) == int :
            self.__NbPage = nbpage
        else:
            print(f"La valeur entrer n'est pas valide")
    
    def verification(self):
        return self.__Disponible
    
    def emprunter(self):
        if self.verification() == True:
            self.__Disponible = False
        else :
            print(f"Le livre {self.__Titre} est deja emprunter")
    
    def rendre(self):
        if self.verification() == False:
            self.__Disponible = True
        else :
            print(f"Le livre {self.__Titre} n'est pas emprunter")