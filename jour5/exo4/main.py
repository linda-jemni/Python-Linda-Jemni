from tkinter import * 
from formulaire import * 

new_conn = create_connection("tt_user.db")


vider_Bdd(new_conn) 

personne_id = ajouterPersonne(new_conn,('linda','linda123'))


def Verification(): 
	if (): 
		messagebox.showinfo("connection" , "utilisateur connecté")
	else: 
		messagebox.showinfo("connection" , "erreur de connection")


fenetrePrincipale = Tk ()

l = Label(fenetrePrincipale, text= "Login")
e= Entry(fenetrePrincipale)
l.pack()
e.pack()

p = Label(fenetrePrincipale, text= "Password")
e= Entry(fenetrePrincipale)
p.pack()
e.pack()

b = Button (fenetrePrincipale, text= "Login" ) 
b.pack()

fenetrePrincipale.mainloop()





