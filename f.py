import sqlite3

class DB :
    def __init__(self, base: str) :
        self.connection = sqlite3.connect(base)
        self.new_c()
    
    def new_c(self) :
        self.cursor = self.connection.cursor()
        
    def write_products (self) :
        cur = self.cursor
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
       
        otv = []
        for row in rows :
            otv.append(row[1]) 
        
        return otv
    
    def write_klienti(self) :
        cur = self.cursor
        cur.execute("SELECT * FROM klienti")
        rows = cur.fetchall()
       
        otv = []
        for row in rows :
            otv.append(row[1]) 
        
        return otv    
    
    def write_products_klienti(self, name) :
        cur = self.cursor
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
        
        return otv         
    
    def zena_pokupki_za_vse_vreme(self, name) :

        cur = self.cursor       
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
                    
        a = [str(zena)]
        return a
    
    def __del__(self) :
        self.connection.close()    

p = DB('sqlite.db')
print(p.zena_pokupki_za_vse_vreme('Petr Nikolaevich'))