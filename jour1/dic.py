d = {"Bonjour":"Good Morning","Salut":"Hi","Bonne nuit":"Good Night"}
print (d)
e = str(input("entrer un mot"))
e2 =str(input("entrer sa traduction en anglais"))

d[e] =e2
print(d)

d1  = {}

e3 =str(input("choisis une lettre"))

to_del = [key for key in fr_ang if key.startswith(e3)] 
for key in to_del: del fr_ang[key]


print ("Tous les mots qui contiennent la lettre ", e3 , "sont supprimées")