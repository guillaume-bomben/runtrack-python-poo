class CompteBancaire:
    def __init__(self,id,nom,prenom,solde,decouvert):
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def get_solde(self):
        return self.__solde
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def afficher(self):
        print(f"Compte de {self.__nom} {self.__prenom} : \n Solde : {self.__solde} € \n id : {self.__id}")
    
    def afficherSolde(self):
        print(f"Solde restant : {self.__solde} €")
    
    def versement(self,ammount):
        if type(ammount) != int:
            print("Le montant saisie n'est pas un entier")
        else :
            self.__solde += ammount
    
    def retrait(self,ammount):
        if type(ammount) != int:
            print("Le montant saisie n'est pas un entier")
        elif ammount > self.__solde and self.__decouvert == False:
            print(f"Il n'y a pas asser d'argent sur le compte")
        else:
            self.__solde -= ammount
    
    def agios(self):
        if self.__solde < 0 :
            self.__solde +=1000
    
    def virement(self,compte,ammout):
        if type(compte) == CompteBancaire and type(ammout) == int:
            compte.versement(ammout)
            print(f"Le virement de {ammout} € du compte {self.__nom} {self.__prenom} vers le compte de {compte.get_nom()} {compte.get_prenom()}")
        else:
            print(f"Il n'est pas possible de faire ce virement")