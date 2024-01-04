class Personne:
    def __init__(self,nom,age,obj):
        self.__nom = nom
        self.__age = age
        self.__obj = obj
        self.nbpersonne = 1
        self.ajouter_personne()
    
    def ajouter_personne(self):
        self.__obj._Ville__nbhabitant += 1
        