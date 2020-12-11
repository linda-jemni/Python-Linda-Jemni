# Lecture / Ecriture objet dans fichier

import pickle
class Player:
	def __init__(self,name,level):
		self.name = name
		self.level = level

	def whoami(self):
		print("{} ({})".format(self.name, self.level))

#Programme principal
#création de mon objet
p1 = Player("Eddy",175)
# enregistrement de l'objet créé dans le fichier player.data
# wb = write binary
"""
with open("player.data","wb") as fic:
	record = pickle.Pickler(fic)
	record.dump(p1)
"""

with open("player.data","rb") as fic:
	get_record = pickle.Unpickler(fic)
	player_one = get_record.load()

player_one.whoami()

