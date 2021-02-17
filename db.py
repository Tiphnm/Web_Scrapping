import mysql.connector
from webscrap import *

database = mysql.connector.connect(host="scrap_sql",database= "Maison_du_Monde",user="root",password="123")

class Table: 
    def __init__(self):
        logging.info('Initiating my class: start')
        self.mycursor= database.cursor()
        logging.info('Initiating my class: end')

    def erase_table(self):
        logging.info('Deleting my tables to not repeat rows: start')
        self.mycursor.execute("DROP Table Carpet")
        #self.mycursor.execute("DROP Table Mirror")
        database.commit()
        logging.info('Deleting my tables to not repeat rows: end')

    def create_table(self):
        logging.info('Creating my Tables: start')

        self.mycursor.execute("CREATE TABLE IF NOT EXISTS Carpet (ID INT PRIMARY KEY AUTO_INCREMENT, NOM VARCHAR(255), PRIX VARCHAR(30))")

        #self.mycursor.execute("CREATE TABLE IF NOT EXISTS Mirror (ID INT PRIMARY KEY AUTO_INCREMENT, NOM VARCHAR(255), PRIX VARCHAR(30))")
        database.commit()

        logging.info('Creating my Tables: end')

    def insert_info(self):
        logging.info('Inserting my data from my webscrapping: start')
        carpet_sql = "INSERT INTO Carpet (NOM, PRIX) VALUES (%s,%s)"
        carpet_valeur = c.zip_list_carpet()
        self.mycursor.executemany(carpet_sql, carpet_valeur)
        
        #mirror_sql = "INSERT INTO Mirror (NOM, PRIX) VALUES (%s,%s)"
        #mirror_valeur = m.zip_list_mirror()
        #print(mirror_valeur)
        #self.mycursor.executemany(mirror_sql, mirror_valeur)

        database.commit()
        logging.info('Inserting my data from my webscrapping: end')

t = Table()
t.erase_table()
t.create_table()
t.insert_info()

