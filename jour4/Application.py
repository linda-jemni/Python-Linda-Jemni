from tkinter import *
 
###################################################################################
# Classe définissant l'objet représentant la fenêtre principale de l'application
###################################################################################
class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Application!")   # Le titre de la fenêtre
        
        self.minsize(1550,850)      #taille de fenêtre
        
        # Une méthode séparée pour construire le contenu de la fenêtre
        self.createWidgets()
 
    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()      # Choix du mode d'arrangement
       
        # Création des widgets
        # ...........
        # ...........
        # ...........
 
        # Un bouton pour quitter l'application
        self.quitButton = Button(self, text = "Quitter", 
                                 command = self.destroy)
        self.quitButton.grid()
 
    # D'autres méthodes ....
    # ......................
 
app = Application()
app.mainloop()