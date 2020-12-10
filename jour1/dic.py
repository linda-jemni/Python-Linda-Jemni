d = {"Bonjour":"Good Morning","Salut":"Hi","Bonne nuit":"Good Night"}
print (d)
e = str(input("entrer un mot"))
e2 =str(input("entrer sa traduction en anglais"))

d[e] =e2
print(d)

d1  = {}

e3 =str(input("choisis une lettre"))

d1 = {}
for i in d.keys () :
	if i[0] != e3 :
		d1 [i] = d[i]
print (d1)

print ("Tous les mots qui contiennent la lettre ", e3 , "sont supprimées")