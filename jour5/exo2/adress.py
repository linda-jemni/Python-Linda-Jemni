
class Adress:

    def __init__(self,codePostal,rue,ville):
        self.__codePostal = codePostal
        self.__ville = ville
        self.__rue = rue
    
    @property
    def codePostal(self):
        return self.__codePostal

    @property
    def ville(self):
        return self.__ville

    @property  
    def rue(self):
        return self.__rue
    
    @codePostal.setter
    def codePostal(self,v):
        self.__codePostal = v
    
    @ville.setter
    def ville(self,v):
        self.__ville = v
    
    @rue.setter
    def rue(self,r):
        self.__rue = r

    def __str__(self):
        return ("Adress [ville : {} , rue: {} , codePostal: {}] ".format(self.__ville,self.__rue,self.__codePostal))