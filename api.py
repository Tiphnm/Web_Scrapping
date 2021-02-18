from main import *
from flask import Flask, render_template, jsonify
import mysql.connector



app = Flask(__name__)

conn = mysql.connector.connect( host='scrap_sql',
                                database='Maison_du_Monde',
                                user='root',
                                password='123',
                                )
sql_query = conn.cursor()

@app.route('/home_page')
def welcome(): 
    return "Welcome to Maison Du Monde's API ! "    

@app.route('/api')
def api():
    conn = mysql.connector.connect( host='scrap_sql',
                                database='Maison_du_Monde',
                                user='root',
                                password='123',
                                )
    sql_query = conn.cursor()
    sql_query.execute("SELECT * FROM Carpet, Mirror WHERE Carpet.ID = Mirror.ID ORDER BY Carpet.ID")
    output = sql_query.fetchall()
    return jsonify(output)


@app.route('/api_carpet')
def api_carpet(): 
    conn = mysql.connector.connect( host='scrap_sql',
                                database='Maison_du_Monde',
                                user='root',
                                password='123',
                                )
    sql_query = conn.cursor()
    sql_query.execute("SELECT * FROM Carpet")
    output = sql_query.fetchall()
    return jsonify(output)

@app.route('/api_mirror')
def api_mirror(): 
    conn = mysql.connector.connect( host='scrap_sql',
                                database='Maison_du_Monde',
                                user='root',
                                password='123',
                                )
    sql_query = conn.cursor()
    sql_query.execute("SELECT * FROM Mirror")
    output = sql_query.fetchall()
    return jsonify(output)

if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=3050, debug = True)