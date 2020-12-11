from bdd import *

new_conn = create_connection("db_exo1.db")

if new_conn is None:
    raise Exception("Error! cannot create the database connection.")

vider_Bdd(new_conn) 


client1_id = ajouterClient(new_conn,"Linda","jemni","35 rue jean bleuzen","Femme")
client2_id = ajouterClient(new_conn,"alice","picard","40 rue jean jaures","Femme")
client3_id = ajouterClient(new_conn,"gerard","leloup","champs elysée","Homme")

agence1_id = ajouterAgence(new_conn,"BNPP")
agence2_id = ajouterAgence(new_conn,"credit agricole")
agence3_id = ajouterAgence(new_conn,"lcl")

compte1_client1 = ajouterCompte(new_conn,0,180,client1_id,agence1_id)
compte1_client2 = ajouterCompte(new_conn,10,500,client2_id,agence2_id)
compte2_client1 = ajouterCompte(new_conn,500,2000000,client1_id,agence1_id)
compte1_client3 = ajouterCompte(new_conn,10000,300000,client3_id,agence1_id)
compte3_client1 = ajouterCompte(new_conn,300,10000000,client1_id,agence1_id)

#READ FUNCTIONS test

print ('\n'.join([ str(myelement) for myelement in listerComptes(new_conn) ])) 
print ('\n'.join([ str(myelement) for myelement in listerComptes(new_conn,compte2_client1) ])) 
print ('\n'.join([ str(myelement) for myelement in listerAgence(new_conn) ])) 

print ('\n'.join([ str(myelement) for myelement in listerClient(new_conn) ])) 
print (listerClient(new_conn,'Linda','Jemni')) 

modifierClient(new_conn,{
    'id': client3_id,
    'nom': 'modified name 3',
    'prenom': 'modified prenom 3',
    'Civilite': 'Homme',
    'adresse': '100 rue la marche rouge'
})
print (listerClient(new_conn,'modified name 3','modified prenom 3')) 

modifierAgence(new_conn,{
    'id': agence3_id,
    'nomAgence': 'modified agence 3'
})
print (listerAgence(new_conn,'modified agence 3') ) 


modifierCompteBancaire(new_conn,{
    'id': compte1_client1,
    'decouvert' : 500, 
    'solde' : 1000
})

print ('\n'.join([ str(myelement) for myelement in listerComptes(new_conn,compte1_client1) ]))

ajouter(new_conn,listerClient(new_conn,client1_id)[0],listerComptes(new_conn,compte1_client1)[0],1400)
print(" ///////////////////////aprés avoir ajouter /////////////////")
print ('\n'.join([ str(myelement) for myelement in listerComptes(new_conn,compte1_client1) ]))


retirer(new_conn,listerClient(new_conn,client1_id)[0],listerComptes(new_conn,compte1_client1)[0],500)
print("==================== Aprés avoir ajouter ///////////////////")
print ('\n'.join([ str(myelement) for myelement in listerComptes(new_conn,compte1_client1) ]))

retirer(new_conn,listerClient(new_conn,client1_id)[0],listerComptes(new_conn,compte1_client1)[0],5000)


print ('\n'.join([ str(compte) for compte in listerCompteAgence(new_conn,{
    'nomAgence': 'BNP'
}) ]))


print ('\n'.join([ str(compte) for compte in listerCompte(new_conn,{
    'idClient': client1_id
}) ]))

