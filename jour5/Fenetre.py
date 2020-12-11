# Fenetre
import tkinter
from tkinter.messagebox import *

def verification ():
	# si le mot correspond à celui attendu
	if var_entry.get() == 'toto':
		showinfo('Résultat','Mot de passe correct.\nAu revoir !')
	else:
		showwarning('Résultat','Mot de passe incorrect.\nVeuillez recommencer !')
		var_entry.set('')

	# sinon
"""
StringVar(): chaine de caractère
IntVar() : nombre entier
DoubleVar(): nombre à virgule
BooleanVar() : booléen
"""
#Création de la fenetre globale
root = tkinter.Tk()
#Paramétrer la fenetre globale
root.geometry("400x400")
root.title("Ma Fenetre tkinter")
 
# Initialiser les widgets à afficher (ex Label)

#création menu principal
mainmenu = tkinter.Menu(root)
#création du premier sous-menu
first_menu = tkinter.Menu(mainmenu,tearoff=0)
first_menu.add_command(label="Option1")
first_menu.add_command(label="Option2")
first_menu.add_command(label="Quitter", command=root.quit)
#création du deuxième sous-menu
second_menu = tkinter.Menu(mainmenu,tearoff=0)
second_menu.add_command(label="Commande1")
second_menu.add_command(label="Commande2")
#Donner l'ordre d'apparition des sous-menu dans la fenetre
mainmenu.add_cascade(label="Premier",menu=first_menu)
mainmenu.add_cascade(label="Second",menu=second_menu)
#Label
w = tkinter.Label(root, text = "Hello, tout le monde!")
#Zone de Saisie
var_entry = tkinter.StringVar()
entry = tkinter.Entry(root,textvariable=var_entry)
# Bouton
bouton = tkinter.Button(root,text='Valider', command=verification)
var_gender = tkinter.IntVar()
radio1 = tkinter.Radiobutton(root,text="Homme",value=1,variable=var_gender)
radio2 = tkinter.Radiobutton(root,text="Femme",value=0,variable=var_gender)

# appliquer le mode d'affichage
w.pack()
entry.pack()
radio1.pack()
radio2.pack()
bouton.pack()
# Affichage de la fenetre Globle
root.config(menu=mainmenu)
root.mainloop()