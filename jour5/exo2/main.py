from personne import Personne
from adress import Adress
from listePersonnes import ListPersonnes

print("="*20 + "Create adresses" +"="*20)
print("\n")

adress1 = Adress("92170","vanves ","ile de france")
adress2 = Adress("75009","35 rue jean bleuzen","Puteaux")
adress3 = Adress("75014", "Garenne Colombes" , "ile de france")


print("="*20 + "Creer personnes"+"="*20)
print("\n")

personne1 = Personne("Linda","F")
personne2 = Personne("Gerard","M")

print("="*20 + "Ajouter Adresses personnes" +"="*14)
print("\n")

personne1.add_adress(adress1)
personne1.add_adress(adress2)
personne2.add_adress(adress3)

print("="*20 + "LIST PERSONS" +"="*20)
print("\n")

print(personne1)

listePersonnes1 = ListPersonnes()
listePersonnes1.addPersonne(personne1)
listePersonnes1.addPersonne(personne2)


print("="*20 + "Update Persons City" +"="*20)
print("\n")

listePersonnes1.edit_personne_ville("safae","paris")
print(listePersonnes1)


print("="*20 + "Update Persons NAME" +"="*20)
print("\n")

listePersonnes1.edit_personne_nom("Linda","Nour")
print(listePersonnes1)

print("\n")
print("="*20 + "Nombre d'objet avc ville 'Paris" +"="*20)
print("\n")

number = listePersonnes1.count_personne_ville('paris')
print(number)

print("\n")
print("="*20 + "Exists code Postal 90 000" +"="*20)
print("\n")

print(listePersonnes1.exists_code_postal("90 000"))

print("\n")
print("="*20 + "Exists nom Mat" +"="*20)
print("\n")

print(listePersonnes1.find_by_nom("Zack"))

print("\n")
print("="*20 + "ecrire dans le fichier" +"="*20)
print("\n")

listePersonnes1.write_in_file()

print("="*20 + "lire du fichier" +"="*20)
print('\n'.join(str(elem) for elem in listePersonnes1.read_from_file()))