from Personne import Personne

class Professeur(Personne):
    def __init__(self,matiereEnseignée):
        super().__init__()
        self.__matiereEnseignée = matiereEnseignée
    
    def enseigner(self):
        print("Le cours va commencer")