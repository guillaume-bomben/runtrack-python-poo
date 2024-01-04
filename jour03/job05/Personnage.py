import random

class Personnage:
    def __init__(self,name,life):
        self.name = name
        self.life = life
        
    def attaquer(self,enemy):
        damage = random.randint(1,10)
        print(f"{self.name} attaque {enemy.name} et lui inflige {damage} points de degats")
        enemy.life -= damage
        print(f"Il reste {enemy.life} HP a {enemy.name}")