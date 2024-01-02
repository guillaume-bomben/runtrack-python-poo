class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenon = prenom
    
    def SePresenter(self):
        print(f"Je suis {self.nom} {self.prenon}")