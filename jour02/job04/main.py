from Student import Student

s1 = Student("John","Doe",145)
s1.add_credits(30)
s1.add_credits(25)
s1.add_credits(60)

print(f"Le nombre de credit de {s1.get_nom()} {s1.get_prenom()} est de {s1.get_credit()} point")

s1.studentInfo()