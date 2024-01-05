class Personne:
    def __init__(self):
        self.age = 14
    
    def afficherAge(self):
        print(f"la personne est agé de {self.age} ans")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self,age):
        self.age = age
    