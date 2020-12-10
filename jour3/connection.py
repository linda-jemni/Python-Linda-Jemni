<<<<<<< HEAD
import sqlite3 

from sqlite3 import Error


def create_connection(db_file):
    connx = None
    try:
        connx = sqlite3.connect(db_file)
        return connx        
    except Error as e:
        print(e)
    return connx


def create_table(conn, create_table_sql):
    try:
        cu = conn.cursor()
        cu.executescript(create_table_sql)
    except Error as e:
        print(e)

if __name__ == '__main__':
=======
import sqlite3 

from sqlite3 import Error


def create_connection(db_file):
    connx = None
    try:
        connx = sqlite3.connect(db_file)
        return connx        
    except Error as e:
        print(e)
    return connx


def create_table(conn, create_table_sql):
    try:
        cu = conn.cursor()
        cu.executescript(create_table_sql)
    except Error as e:
        print(e)

if __name__ == '__main__':
>>>>>>> 802c16b6b2e5fc7057c661b0dbd75eab386584a5
    cnnx = create_connection("dbfile.db")