d = {"Bonjour":"Good Morning","Salut":"Hi","Bonne nuit":"Good Night"}
print (d)
e = str(input("entrer un mot"))
e2 =str(input("entrer sa traduction en anglais"))

d[e] =e2
print(d)

d1  = {}

for k in d.keys () :
	if k[0] != b :
		d1 [k] = d[k]