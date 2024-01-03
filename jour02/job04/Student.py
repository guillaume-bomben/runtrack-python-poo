class Student:
    def __init__(self,nom,prenom,id,credit=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credit = credit
        self.__level = "Insuffisant"
    
    def add_credits(self,add):
        if add > 0 :
            self.__credit += add
            self.__studentEval__()
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_id(self):
        return self.__id
    
    def get_credit(self):
        return self.__credit
    
    def __studentEval__(self):
        if self.__credit >= 90:
            self.__level = "Excellent"
        if 90 > self.__credit >= 80:
            self.__level = "Tres Bien"
        if 80 > self.__credit >= 70:
            self.__level = "Bien"
        if 70 > self.__credit >= 60:
            self.__level = "Passable"
        if self.__credit < 60:
            self.__level = "Insuffisant"
    
    def studentInfo(self):
        print(f"Nom = {self.__nom}")
        print(f"Prenom = {self.__prenom}")
        print(f"id = {self.__id}")
        print(f"Niveau = {self.__level}")