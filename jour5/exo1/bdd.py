from connection import create_connection,create_table

new_conn = create_connection("db_exo1.db")

if new_conn is None:
    raise Exception("Error! cannot create the database connection.")

sql_create_tables = """ CREATE TABLE "Client" (
                                "idClient"	INTEGER NOT NULL,
                                "Civilite"	TEXT NOT NULL,
                                "nom"	TEXT NOT NULL,
                                "prenom"	TEXT NOT NULL,
                                "adresse"	TEXT NOT NULL,
                                PRIMARY KEY("idClient" AUTOINCREMENT)
                            );
                        CREATE TABLE "CompteBancaire" (
                                "idCompte"	INTEGER NOT NULL,
                                "solde"	INTEGER NOT NULL,
                                "decouvert"	INTEGER NOT NULL,
                                "idClient" INTEGER NOT NULL,
                                "idAgence" INTEGER,
                                PRIMARY KEY("idCompte" AUTOINCREMENT),
                                FOREIGN KEY("idClient") REFERENCES "Client"("idClient"),
                                FOREIGN KEY("idAgence") REFERENCES "Agence"("idAgence")
                            );
                            CREATE TABLE "Agence" (
                                "idAgence"	INTEGER NOT NULL,
                                "nomAgence"	TEXT NOT NULL,
                                PRIMARY KEY("idAgence" AUTOINCREMENT)
                            );"""

#create_table(new_conn, sql_create_tables)

def ajouterClient(conn,nom,prenom,adresse,Civilite):
    sql = ''' INSERT INTO Client(nom,prenom,adresse,Civilite)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (nom,prenom,adresse,Civilite,))
    conn.commit()
    return cur.lastrowid

def ajouterCompte(conn,solde,decouvert,idClient,idAgence):
    sql = ''' INSERT INTO CompteBancaire(solde,decouvert,idClient,idAgence)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (solde,decouvert,idClient,idAgence,))
    conn.commit()
    return cur.lastrowid

def ajouterAgence(conn,nomAgence):

    sql = ''' INSERT INTO Agence(nomAgence)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (nomAgence,))
    conn.commit()
    return cur.lastrowid

def listerComptes(conn,idCompte=None):
    
    cur = conn.cursor()

    if idCompte is not None:
        cur.execute("SELECT * FROM CompteBancaire where idCompte = ?", (idCompte,))
    else:
        cur.execute("SELECT * FROM CompteBancaire")

    desc = cur.description 
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in cur.fetchall()]
    
    return data

def listerAgence(conn,nomAgence=None):
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM Agence")

    desc = cur.description 
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in cur.fetchall()]
    if nomAgence is not None:
        return next((agence for agence in data if agence["nomAgence"] == nomAgence), None)
    else:
        return data

def listerClient(conn,nomClient=None,prenomClient=None):
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM Client")

    desc = cur.description 
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in cur.fetchall()]

    if nomClient is not None and prenomClient is not None :
        return next((client for client in data if client["nom"] == nomClient and client["prenom"] == prenomClient), None)
    else:
        return data




def modifierClient(conn,newRecord):
    if(newRecord['id'] is not None):
        sql = ''' UPDATE Client
                    SET nom = ?, prenom= ?, Civilite = ?, adresse = ?
                    WHERE idClient = ?'''
        cur = conn.cursor()
        cur.execute(sql,(newRecord['nom'],newRecord['prenom'],newRecord['Civilite'],newRecord['adresse'],newRecord['id']))
        conn.commit()
    return
    

def modifierAgence(conn,newRecord):
    if(newRecord['id'] is not None):
        sql = ''' UPDATE Agence
                    SET nomAgence = ?
                    WHERE idAgence = ?'''
        cur = conn.cursor()
        cur.execute(sql,(newRecord['nomAgence'],newRecord['id']))
        conn.commit()
    return

def modifierCompteBancaire(conn,newRecord):
    if(newRecord['id'] is not None):
        sql = ''' UPDATE CompteBancaire
                    SET decouvert = ?,
                    solde = ?
                    WHERE idCompte = ?'''
        cur = conn.cursor()
        cur.execute(sql,(newRecord['decouvert'],newRecord['solde'],newRecord['id']))
        conn.commit()
    return

 

def supprimerClient(conn,idClient):
    sql = 'DELETE FROM Client WHERE idClient=?'
    cur = conn.cursor()
    cur.execute(sql, (idClient,))
    conn.commit()

def supprimerAgence(conn,idAgence):
    sql = 'DELETE FROM Agence WHERE idAgence=?'
    cur = conn.cursor()
    cur.execute(sql, (idAgence,))
    conn.commit()

def supprimerCompte(conn,idCompte):
    sql = 'DELETE FROM CompteBancaire WHERE idCompte=?'
    cur = conn.cursor()
    cur.execute(sql, (idCompte,))
    conn.commit()

def vider_Bdd(conn):
    c = conn.cursor()

    c.execute('DELETE FROM CompteBancaire;',)
    c.execute('DELETE FROM Agence;',)
    c.execute('DELETE FROM Client;',)

    print(" les tables sont supprimées  !")
    conn.commit()



def ajouter(conn,client,compte,solde):
    if client['idClient'] is not None:
        sql = ''' UPDATE CompteBancaire
                    SET solde = ?
                    WHERE idClient = ?'''
        oldSolde = compte['solde']
        newSolde = oldSolde + solde

        
        modifierCompteBancaire(conn,{
            'id': compte['idCompte'],
            'solde': newSolde,
            'decouvert': compte['decouvert']
        })
    return newSolde



def retirer(conn,client,compte,solde):
    if client['idClient'] is not None:
        compte_desc = listerComptes(conn,compte['idCompte'])[0]

        if(compte_desc['solde']-solde < compte_desc['decouvert']):
            print("impossible to withdraw money from yout account newSolde < decouvert autorisée")
            return False
        
        oldSolde = compte['solde']
        newSolde = int(oldSolde) - solde
        
        modifierCompteBancaire(conn,{
            'id': compte_desc['idCompte'],
            'solde': newSolde,
            'decouvert': compte_desc['decouvert']
        })
    return True



def listerCompteAgence(conn,agence):

    cur = conn.cursor()
    cur.execute("SELECT * FROM CompteBancaire cb where cb.idAgence = (select idAgence from Agence where nomAgence= ?)", (agence['nomAgence'],))

    rows = cur.fetchall()
    return rows


def listerCompte(conn,client):

    cur = conn.cursor()
    cur.execute("SELECT * FROM CompteBancaire cb where cb.idClient = ?", (client['idClient'],))

    rows = cur.fetchall()
    return rows








        