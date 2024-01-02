from Produit import Produit

p1 = Produit("riz",10,20)
print(p1.afficher())

p1.changeNom("thon")
print(p1.afficherNom())

p1.changeTVA(15)
print(p1.afficherTVA())


p1.changePrixHT(20)
print(p1.afficherPrixHT())

print(p1.afficherPrixTTC())