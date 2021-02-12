import sqlite3
from webscrap import *

conn = sqlite3.connect("my_db.db")

CarpetList = name_carpet()
#print(CarpetList)

CarpetPrice = price_carpet()
#print(CarpetPrice)

conn = sqlite3.connect("my_db.db")
c = conn.cursor()

def create_db():
    c.execute("DROP TABLE carpet")
    c.execute("CREATE TABLE IF NOT EXISTS carpet ( id INTEGER PRIMARY KEY NOT NULL, carpet_name VARCHAR(100),price VARCHAR(30))")
    c.execute("INSERT INTO carpet Values(1,'Nom','prix')")
    c.execute("SELECT * FROM carpet")
    conn.commit()

    # Remember to save + close

create_db()

def read_from_db():
    c.execute ('SELECT * FROM carpet ') 
for row in c.fetchall():
    print(row)

read_from_db()