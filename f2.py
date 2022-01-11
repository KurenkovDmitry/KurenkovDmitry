import sqlite3

con = sqlite3.connect('sqlite.db')

with con :
    cur = con.cursor()
    cur.execute("SELECT * FROM klienti")
    rows = cur.fetchall()
   
    otv = []
    for row in rows :
        otv.append(row[1]) 

print(otv)

con.close()