from Voiture import Voiture

v1 = Voiture("fiat","500",95,200)
print(v1.get_en_marche())

v1.demarrer()
print(v1.get_en_marche())

v1.arreter()
print(v1.get_en_marche())