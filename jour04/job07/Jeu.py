import random
from Carte import Carte

class Jeu(Carte):
    def __init__(self, valeur, couleur):
        super().__init__(valeur, couleur)
    
    def game(self):
        joueur = [] ; valJ = 0
        croupier = [] ; valC = 0
        
        joueur.append(random.choice(list(self.paquet.keys())))
        joueur.append(random.choice(list(self.paquet.keys())))
        
        croupier.append(random.choice(list(self.paquet.keys())))
        croupier.append(random.choice(list(self.paquet.keys())))
        
        for jcarte in joueur:
            valJ += self.ValCard(jcarte)
        for ccarte in croupier:
            valC += self.ValCard(ccarte)
            
        print(f"Main du joueur : {joueur} -> Score : {valJ}")
        print(f"Main du croupier : {croupier} -> Score : {valC}")
        
        choix = input(f"Votre Score est de {valJ} , Voulez vous continuer (O/N) : ")
        while choix.lower() != "n":
            ncard = random.choice(list(self.paquet.keys()))
            joueur.append(ncard)
            valJ += self.ValCard(ncard)
            print(f"Main du joueur : {joueur} -> Score : {valJ}")
            choix = input(f"Votre Score est de {valJ} , Voulez vous continuer (O/N) : ")
        while valC < 17:
            ncard = random.choice(list(self.paquet.keys()))
            croupier.append(ncard)
            valC += self.ValCard(ccarte)
        print(f"Main du croupier : {croupier} -> Score : {valC}")
        
        if valC <= 21 and valJ <= 21 :
            if valJ > valC:
                print("Le joueur a gagner")
            elif valJ < valC:
                print("Le croupier a gagner")
            else:
                print("Le joueur et le croupier sont a égaliter")
        elif valC <=21 :
            print("Le croupier a gagner")
        elif valJ <=21:
            print("Le joueur a gagner")
        else:
            print("Le croupier et le joueur on perdu")