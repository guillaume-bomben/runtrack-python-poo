class Joueur:
    def __init__(self,nom,numero,position,nbbut,passde,cjaune,crouge):
        self.Nom = nom
        self.Numero = numero
        self.Position = position
        self.NbBut = nbbut
        self.PassDe = passde
        self.CJaune = cjaune
        self.CRouge = crouge
    
    def marquerUnBut(self):
        self.NbBut += 1
    
    def effectuerUnePasseDecisive(self):
        self.PassDe += 1
    
    def recevoirUnCartonJaune(self):
        self.CJaune += 1
    
    def recevoirUnCartonRouge(self):
        self.CRouge += 1
    
    def afficherStatistiques(self):
        print(f"Non : {self.Nom}")
        print(f"Numero : {self.Numero}")
        print(f"Position : {self.Position}")
        print(f"Buts marqués  : {self.NbBut}")
        print(f"Passes décisives effectuées : {self.PassDe}")
        print(f"cartons jaunes : {self.CJaune}")
        print(f"cartons rouge : {self.CRouge}")
        print("------------------------------------------------------")