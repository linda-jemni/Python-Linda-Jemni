from personne import Personne
import pickle

class ListPersonnes:

    def __init__(self):
        self.__personnes = []
    
    def addPersonne(self,p):
        self.__personnes.append(p)
    
    def getPersonnes(self):
        return self.__personnes
    
    def removePersonne(self,p):
        if p in self.__personnes :
            self.__personnes.remove(p)
        else:
            print("La personne {} n'existe pas dans la liste".format(p))
    
    def find_by_nom(self,s):
        for personne in self.__personnes :
            if personne.nom == str(s) :
                return str(personne)
        return None
    def exists_code_postal(self,c):
        for personne in self.__personnes :
            for adr in personne.getAdress():
                if adr.codePostal == c :
                    return True
                else :
                    return False

    def count_personne_ville(self,ville):
        count = 0
        for personne in self.__personnes :
            for adr in personne.getAdress():
                if adr.ville == ville :
                    count = count + 1
        return count

    def edit_personne_nom(self,oldNom,newNom) :
        for personne in self.__personnes :
            if personne.nom == oldNom:
                personne.nom = newNom

    def edit_personne_ville(self,nom,newVille):
        for personne in self.__personnes :
            if personne.nom == nom:
                for adr in personne.getAdress():
                    adr.ville = newVille

    def __str__(self):
        return ("Liste Personnes : \n {} ".format('\n'.join([str(per) for per in self.__personnes])))

    def write_in_file(self):
        with open("personnes.data","w") as fic:
            for person in self.__personnes:
                fic.write('%s\n' % person)
        print("les personnes sont enregistrées")
        fic.close()

    
    def read_from_file(self):
        personnes = []
        with open("personnes.data","r") as fic:
            for line in fic:
                personnes.append(line)
        fic.close()
        return personnes

    