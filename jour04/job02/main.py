from Personne import Personne
from Eleve import Eleve
from Professeur import Professeur

p1 = Personne()
e1 = Eleve()
pro1 = Professeur("philo")

e1.bonjour()
e1.allerEnCours()
e1.modifierAge(15)

pro1.modifierAge(40)
pro1.bonjour()
pro1.enseigner()