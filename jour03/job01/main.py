from Ville import Ville
from Personne import Personne

Paris = Ville("Paris",1000000)
print(f"Population de la ville de {Paris.get_name()} : {Paris.get_nbhabitant()} habitants")

Marseille = Ville("Marseille",861635)
print(f"Population de la ville de {Marseille.get_name()} : {Marseille.get_nbhabitant()} habitants")

John = Personne("John",45,Paris)
Myrtille = Personne("Myrtille",4,Paris)
Chloe = Personne("Chloe",18,Marseille)

print(f"Mise a jour de la popuplation de la ville de {Paris.get_name()} : {Paris.get_nbhabitant()} habitants")
print(f"Mise a jour de la popuplation de la ville de {Marseille.get_name()} : {Marseille.get_nbhabitant()} habitants")