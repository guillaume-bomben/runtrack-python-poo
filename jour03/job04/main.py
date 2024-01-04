from Joueur import Joueur
from Equipe import Equipe

OM = Equipe("OM")
PSG = Equipe("PSG")

j1 = Joueur("j1",10,"atk",0,0,0,0)
j2 = Joueur("j2",1,"def",0,0,0,0)
j3 = Joueur("j3",11,"mil",0,0,0,0)
j4 = Joueur("j4",5,"def",0,0,0,0)
j5 = Joueur("j5",15,"def",0,0,0,0)

OM.ajouterJoueur(j1)
OM.ajouterJoueur(j2)
OM.ajouterJoueur(j3)

PSG.ajouterJoueur(j4)
PSG.ajouterJoueur(j5)

OM.AfficherStatistiquesJoueurs()
PSG.AfficherStatistiquesJoueurs()