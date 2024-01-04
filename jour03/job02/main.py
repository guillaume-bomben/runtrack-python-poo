from CompteBancaire import CompteBancaire

c1 = CompteBancaire(1,"John","Doe",500,True)
c1.afficher()
c1.afficherSolde()

c1.versement(100)
c1.afficherSolde()

c1.retrait(50)
c1.afficherSolde()

c1.retrait(1000)
c1.retrait("bonjour")

c2 = CompteBancaire(2,"Tom","Clavis",-100,True)
c1.virement(c2,150)