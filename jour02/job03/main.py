from Livre import Livre

l1 = Livre("SW1","GL",500)
print(l1.verification())

l1.rendre()
l1.emprunter()
print(l1.verification())
l1.emprunter()
l1.rendre()
print(l1.verification())