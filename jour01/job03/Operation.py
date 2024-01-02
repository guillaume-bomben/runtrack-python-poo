class Operation :
    
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        print(f"le resultat de {self.nombre1} + {self.nombre2} est {self.nombre1 + self.nombre2}")