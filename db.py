import mysql.connector
from webscrap import *

database = mysql.connector.connect(host="scrap_sql",database= "Maison_du_Monde",user="root",password="123")

class Table: 
    def __init__(self):
        logging.info('Initiating my class: start')
        self.mycursor= database.cursor()
        logging.info('Initiating my class: end')

    def erase_table(self):
        logging.info('Deleting my table to not repeat rows: start')
        self.mycursor.execute("DROP Table Carpet")
        database.commit()
        logging.info('Deleting my table to not repeat rows: end')

    def create_table(self):
        logging.info('Creating my Carpet Table: start')
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS Carpet (ID INT PRIMARY KEY AUTO_INCREMENT, NOM VARCHAR(255), PRIX VARCHAR(30))")
        database.commit()
        logging.info('Creating my Carpet Table: end')

    def insert_info(self):
        logging.info('Inserting my data from my webscrapping: start')
        sql = "INSERT INTO Carpet (NOM, PRIX) VALUES (%s,%s)"
        valeur = c.zip_list_carpet()
        self.mycursor.executemany(sql, valeur)
        database.commit()
        logging.info('Inserting my data from my webscrapping: end')


t = Table()
#t.erase_table()
#t.create_table()
#t.insert_info()
