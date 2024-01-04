class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self,tache):
        self.taches.append(tache)
    
    def supprimerTache(self,tache):
        self.taches.remove(tache)
    
    def marquerCommeFinie(self,tache):
        tache.statut = "Terminer"
    
    def get_statut(self,tache):
        return tache.statut
    
    def afficherListe(self):
        for t in self.taches :
            print(f"Tache {t.titre} : {t.statut}")
    
    def filterListe(self,statut):
        Ltrier = []
        for t in self.taches :
            if t.statut == statut:
                print(f"Tache {t.titre} : {t.statut}")
                Ltrier.append(t)
        return Ltrier