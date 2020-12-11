class Humain:
	# attributs de classe
	lieu_habitation = "Terre"

	def __init__(self, nom,age):
		self.nom = nom
		self.age = age

	# methode standard
	def parler(self, message):
		print("{} a dit {} ".format(self.nom,message))

	# methode de classe
	@classmethod
	def changer_planete(cls, nouvelle_planete):
		Humain.lieu_habitation = nouvelle_planete

	#changer_planete = classmethod(changer_planete)

	#methode static
	@staticmethod
	def definition():
		print("L'Humain est classé comme l'être vivant le plus évolué")
	#definition = staticmethod(definition)

# PROGRAMME PRINCIPAL
h1 = Humain("jason",25)
print("Planete actuelle : {}".format(Humain.lieu_habitation))
Humain.changer_planete("Mars")
print("Nouvelle actuelle : {}".format(Humain.lieu_habitation))

Humain.definition()

