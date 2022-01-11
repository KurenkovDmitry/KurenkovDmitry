import sqlite3

class DB :
    def __init__(self, base: str) :
        self.connection = sqlite3.connect(base)
        self.new_c()
    
    def new_c(self) :
        self.cursor = self.connection.cursor()
        
    def write_products (self) :
        cur = self.cursor()
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
       
        otv = []
        for row in rows :
            otv.append(row[1]) 
        
        return otv
    
    def __del__(self) :
        self.connect.close()    

p = DB('sqlite.db')
print(p.write_products())