from Livre import Livre

l1 = Livre("Star wars 1","GL",500)
print(l1.get_Titre())
print(l1.get_Auteur())
print(l1.get_NbPage())

l1.set_Titre("ST2")
print(l1.get_Titre())

l1.set_Auteur("DF")
print(l1.get_Auteur())

l1.set_NbPage(-12)
print(l1.get_NbPage())
l1.set_NbPage(15.2)
print(l1.get_NbPage())
l1.set_NbPage(600)
print(l1.get_NbPage())