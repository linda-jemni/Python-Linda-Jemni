from tkinter import * 
from connection import create_connection,create_table


new_conn = create_connection("tt_users.db")


if new_conn is None:
    raise Exception("Error! cannot create the database connection.")

sql_create_tables = """ CREATE TABLE "Personne" (
                                "id"	INTEGER NOT NULL,
                                "login"	TEXT NOT NULL,
                                "password"	TEXT NOT NULL,
                                PRIMARY KEY("idCursus" AUTOINCREMENT)
                            );""" 


def ajouterUser(conn,Personne):

    sql = ''' INSERT INTO Personne(id,login,password)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, etudiant)
    conn.commit()
    return cur.lastrowid


def searchUser(conn):
  
    cur = conn.cursor()
    cur.execute("SELECT * FROM Personne")
    rows = cur.fetchall()
 



