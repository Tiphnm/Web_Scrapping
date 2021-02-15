import mysql.connector
from webscrap import *

database = mysql.connector.connect(
  host="scrap_sql",
  database= "Maison_du_Monde",
  user="root",
  password="123", 
)
mycursor= database.cursor()

def create_table():
    mycursor.execute("CREATE TABLE IF NOT EXISTS Carpet (ID INT PRIMARY KEY AUTO_INCREMENT, NOM VARCHAR(255), PRIX VARCHAR(30))")
    database.commit()
create_table()


def insert_info():
    sql = "INSERT INTO Carpet (NOM, PRIX) VALUES (%s,%s)"
    valeur = final_carpet
    mycursor.executemany(sql, valeur)
    database.commit()
insert_info()
