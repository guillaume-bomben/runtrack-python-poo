class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"Le point a pour coordoner ({self.x},{self.y})")
    
    def afficherX(self):
        print(f"la Coordoner X du point est : {self.x}")
    
    def afficherY(self):
        print(f"la Coordoner Y du point est : {self.y}")
    
    def changerX(self,nx):
        self.x = nx
    
    def changerY(self,ny):
        self.y = ny