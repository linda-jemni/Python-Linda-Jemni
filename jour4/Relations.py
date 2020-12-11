#Tp Relations
class Ville:
	"""Ville"""
	def __init__(self,nomVille):
		self._nomVille = nomVille
		self._batiments = []

	@property
	def nomVille(self):
		return self._nomVille

	@nomVille.setter
	def nomVille(self,v):
		self._nomVille = v
	#Methodes de gestion de la liste des bâtiments
	def get_batiments(self):
		return self._batiments

	def add_batiments(self,b):
		if b not in self._batiments:
			self._batiments.append(b)
	def remove_batiments(self,b):
		if b in self._batiments:
			self._batiments.remove(b)
	#methode demandée
	def liste_villes(self):
		return len(self._batiments)

class Batiment:
	"""Batiments"""
	def __init__(self,nomBat):
		self._nomBat = nomBat
		self._employes = []
	@property
	def nomBat(self):
		return self._nomBat

	@nomBat.setter
	def nomBat(self,b):
		self._nomBat = b

	#Methodes de gestion des employes
	def get_employes(self):
		return self._employes

	def add_employes(self,e):
		if e not in self._employes:
			self._employes.append(e)
	def remove_employes(self,e):
		if e in self._employes:
			self._employes.remove(e)

class Employe:
	"""Employes"""
	def __init__(self,nom,prenom):
		self._nom = nom
		self._prenom = prenom

	@property
	def nom(self):
		return self._nom

	@nom.setter
	def nomBat(self,n):
		self._nom = n
	@property
	def prenom(self):
		return self._prenom

	@nomBat.setter
	def prenom(self,p):
		self._prenom = p

class Entreprise:
	"""Entreprises"""
	def __init__(self,nomEntr):
		self._nomEntr = nomEntr
		self._batiments =[]
		self._villes =[]
	@property
	def nomEntr(self):
		return self._nomEntr

	@nomEntr.setter
	def nomEntr(self,e):
		self._nomEntr = e

	#Methodes de gestion de la liste des bâtiments
	def get_batiments(self):
		return self._batiments

	def add_batiments(self,b):
		if b not in self._batiments:
			self._batiments.append(b)
	def remove_batiments(self,b):
		if b in self._batiments:
			self._batiments.remove(b)

	#Methodes de gestion de la liste des villes
	def get_villes(self):
		return self._villes

	def add_villes(self,v):
		if v not in self._villes:
			self._villes.append(v)
	def remove_villes(self,v):
		if v in self._villes:
			self._villes.remove(v)
