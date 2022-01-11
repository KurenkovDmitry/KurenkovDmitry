import sqlite3

con = sqlite3.connect('sqlite.db')
name = 'Petr Nikolaevich'

with con :
    cur = con.cursor()
    cur.execute("SELECT * FROM klienti")
    rows = cur.fetchall()
   
    id_name = 0
    for row in rows :
        if row[1] == name :
            id_name = row[0]
    
    cur.execute("SELECT * FROM pocupki")
    rows = cur.fetchall()
    
    otv = []
    for row in rows :
        if row[1] == id_name :
            
            otv.append([row[0], row[2], row[3]])
      
    zena = 0
    cur.execute("SELECT * FROM pocupki_items")     
    rows = cur.fetchall()
    for i in range(len(otv)) :
        for row in rows :
            if row[0] == otv[i][0] :
                zena += row[3]
                

print(zena)

con.close()