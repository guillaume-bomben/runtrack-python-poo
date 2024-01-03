class Voiture:
    def __init__(self,marque,modele,annee,km,en_marche=False,reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__en_marche = en_marche
        self.__reservoir = reservoir
    
    #geteur --------------
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_km(self):
        return self.__km
    
    def get_en_marche(self):
        return self.__en_marche
    
    #seter --------------
    def set_marque(self,marque):
        self.__marque = marque
    
    def set_modele(self,modele):
        self.__modele = modele
    
    def set_annee(self,annee):
        self.__annee = annee
    
    def set_km(self,km):
        self.__km = km

    def demarrer(self):
        if self.__verifier_plein__() > 5 :
            self.__en_marche = True
    
    def arreter(self):
        self.__en_marche = False
    
    def __verifier_plein__(self):
        return self.__reservoir