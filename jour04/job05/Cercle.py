from Forme import Forme
from math import *

class Cercle(Forme):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    
    def aire(self):
        return pi * self.radius**2