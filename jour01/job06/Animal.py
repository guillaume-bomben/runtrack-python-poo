class Animal:
    def __init__(self,age=0,prenon=""):
        self.age = age
        self.prenon = prenon
    
    def afficherAge(self):
        print(f"Age de l'animal : {self.age} ans")
    
    def vieillir(self):
        self.age += 1
    
    def nommer(self,prenon):
        self.prenon = prenon
    
    def afficherPrenom(self):
        print(f"L'animal se nome {self.prenon}")