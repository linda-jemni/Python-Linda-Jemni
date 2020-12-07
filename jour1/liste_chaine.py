#coding:utf-8
liste = []
e = str(input("entrer un element"))
liste.append(e) 
q = str(input("la liste est compléte ?"))

if (q == 'non'):
	e = str(input("entrer un element"))
	liste.append(e)  
	q = str(input("la liste est compléte ?"))

for i in liste:
	print("la logeur de" ,i, "est" , len(i))


