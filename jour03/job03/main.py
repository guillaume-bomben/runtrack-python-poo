from ListeDeTaches import ListeDeTaches
from Tache import Tache

t1 = Tache("Course","faire les courses")
t2 = Tache("Menage",'faire le menage')

lt1 = ListeDeTaches()
lt1.ajouterTache(t1)
lt1.ajouterTache(t2)

print(lt1.get_statut(t1))
lt1.marquerCommeFinie(t1)
print(lt1.get_statut(t1))

lt1.afficherListe()
lt1.filterListe("A faire")
lt1.filterListe("Terminer")