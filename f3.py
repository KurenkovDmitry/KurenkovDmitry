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
      
    cur.execute("SELECT * FROM pocupki_items")     
    rows = cur.fetchall()
    for i in range(len(otv)) :
        for row in rows :
            if row[0] == otv[i][0] :
                otv[i][0] = row[1]
                
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    for i in range(len(otv)) :
        for row in rows :
            if row[0] == otv[i][0] :
                otv[i][0] = row[1]

print(*otv, sep = "\n")

con.close()