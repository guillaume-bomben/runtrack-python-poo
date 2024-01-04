class Ville:
    def __init__(self,name,nbhabitant):
        self.__name = name
        self.__nbhabitant = nbhabitant
        
    def get_name(self):
        return self.__name
    
    def get_nbhabitant(self):
        return self.__nbhabitant