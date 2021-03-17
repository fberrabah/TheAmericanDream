import sqlite3 


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


conn = create_connection("Americadbb.db")



q1 = "SELECT * FROM Analyst"


def add_requete(conn, query):
        
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()
    
    i = 0
    for row in rows:
        print(row)
        i += 1
        if i >= 5 :
            break

conn = create_connection("Americadbb.db")

add_requete(conn, q1)