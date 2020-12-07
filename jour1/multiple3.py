n = int(input("Quel est le nombre ?"))
if (n%2 == 0): 
	print("ce nombre est paire")
elif ((n%2 != 0) & (n%3 == 0) ): 
	print ("ce nombre est impair mais multiple de 3")
elif ((n%2 != 0) & (n%3 != 0) ): 
	print ("ce nombre n'est ni pair ni multiple de 3")
