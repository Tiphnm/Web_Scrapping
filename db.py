import sqlite3
import pandas as pd
from webscrap import *


conn = sqlite3.connect("my_db.db")
c = conn.cursor()

label_list = name_carpet()
price_list = price_carpet()

def delete_table():
        c.execute("DROP TABLE carpet")
        conn.commit()

delete_table()

def create_db():
    c.execute("CREATE TABLE IF NOT EXISTS carpet (ID INTEGER PRIMARY KEY, NOM VARCHAR(255) NOT NULL, PRIX VARCHAR(30) NOT NULL)")

create_db()

def insert_db():
    c.executemany("INSERT INTO carpet (NOM, PRIX) VALUES(?, ?) ;", (final_carpet))
    conn.commit()

insert_db()

def read_db():
    Tableau = pd.read_sql_query("SELECT * from carpet", conn)
    print(Tableau)

    '''for row in c.execute("SELECT * FROM carpet"):
        print(row)'''
    conn.close()

result = read_db()






