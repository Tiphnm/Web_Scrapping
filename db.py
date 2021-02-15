import mysql.connector
from webscrap import *

class Table: 
    def __init__(self):
        self.database = mysql.connector.connect(host="scrap_sql",database= "Maison_du_Monde",user="root",password="123")
        self.mycursor= database.cursor()

    def erase_table():
        self.mycursor.execute("DROP table Carpet")
        self.database.commit()

    def create_table():
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS Carpet (ID INT PRIMARY KEY AUTO_INCREMENT, NOM VARCHAR(255), PRIX VARCHAR(30))")
        self.database.commit()

    def insert_info():
        sql = "INSERT INTO Carpet (NOM, PRIX) VALUES (%s,%s)"
        valeur = c.zip_list()
        self.mycursor.executemany(sql, valeur)
        self.database.commit()

t = Table()
t.erase_table()
t.create_table()
t.insert_info()
