class Equipe:
    def __init__(self,nom):
        self.nom = nom
        self.Liste_Joueur = []
    
    def ajouterJoueur(self,joueur):
        self.Liste_Joueur.append(joueur)
    
    def AfficherStatistiquesJoueurs(self):
        for joueur in self.Liste_Joueur:
            joueur.afficherStatistiques()
    
    def mettreAJourStatistiquesJoueur(self,joueur,but,passe,cjaune,crouge):
        joueur.NbBut = but
        joueur.PassDe = passe
        joueur.CJaune = cjaune
        joueur.CRouge = crouge