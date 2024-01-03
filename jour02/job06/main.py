from Commande import Commande

lplat = {"riz":10,"patte":7.5}
l1 = Commande(1,lplat)

print(l1.total_payer())

l1.add_plat({"steak":12})

print(l1.total_payer())