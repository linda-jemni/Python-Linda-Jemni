#coding:utf-8
d = str(input("Indiquer la devise "))
m = int(input("Quel est le montant a convertir ?"))

if (d == '€'): 
	print(m, "euro", m*1.21, "dollars")
else:
	print("le montant est deja en dollars")