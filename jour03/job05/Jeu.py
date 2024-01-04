from Personnage import Personnage

class Jeu:
    def __init__(self):
        self.niveau = 1
    
    def choisirNiveau(self):
        self.niveau = int(input("Entrez un niveau de dificulter (Facile -> 1 / Moyen -> 2 / Difficile -> 3) : "))
    
    def lancerJeu(self):
        self.choisirNiveau()
        
        joueur = Personnage("joueur",self.niveau * 10)
        enemy = Personnage("enemy",self.niveau * 10)
        
        while joueur.life > 0 and enemy.life > 0 :
            joueur.attaquer(enemy)
            if enemy.life < 0 :
                break
            enemy.attaquer(joueur)
        
        if joueur.life > 0:
            print(f"Le joueur a gagner")
        if enemy.life > 0:
            print(f"L'enemy a gagner")