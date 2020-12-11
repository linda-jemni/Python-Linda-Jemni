#Test surcharge
class Surcharge:
	def __init__(self,arg1=None,arg2=None):
		if arg1 and arg2:
			# traitement si arg1 et arg2
			self.arg1 = arg1
			self.arg2 = arg2
		else:
			print("création objet sans attributs")


#PROGRAMME
s1 = Surcharge()
s2 = Surcharge(12,45)

print(s1.__dict__)
print("-----------------------------------")
print(s2.__dict__)