class Commande:
    def __init__(self,nc,lpc):
        self.__nc = nc
        self.__lpc = lpc
        self.__statut = "En Cours"
    
    def add_plat(self,plat):
        self.__lpc.update(plat)
    
    def annuler(self):
        self.__statut = False
    
    def __total__(self):
        for prix in self.__lpc.values():
            self.__total += prix
        return self.__total
    
    def total_payer(self):
        self.__total = 0
        return self.__total__()
    
    