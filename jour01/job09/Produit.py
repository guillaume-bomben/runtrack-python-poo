class Produit:
    def __init__(self,nom,prixHT,TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.tva = TVA
    
    def changeNom(self,nnom):
        self.nom = nnom
    
    def changePrixHT(self,nprixht):
        self.prixHT = nprixht
    
    def changeTVA(self,ntva):
        self.tva = ntva
    
    def CalculerPrixTTC(self):
        return self.prixHT * ((self.tva + 100)/100)

    def afficherNom(self):
        return self.nom

    def afficherPrixHT(self):
        return self.prixHT

    def afficherTVA(self):
        return self.tva

    def afficherPrixTTC(self):
        return self.CalculerPrixTTC()
    
    def afficher(self):
        return f"{self.nom} : \n Prix HT : {self.prixHT} € \n TVA : {self.tva} % \n PrixTTC : {self.CalculerPrixTTC()} €"