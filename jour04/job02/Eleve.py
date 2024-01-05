from Personne import Personne

class Eleve(Personne):
    def __init__(self):
        super().__init__()
    
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")