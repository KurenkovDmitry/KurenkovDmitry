import unittest
from base import DB

class test(unittest.TestCase) :
    @classmethod
    def SetUpClass(cls) -> None :
        cls.database = DB("sqlite.db")
    
    def test_write_products(self) :
        otv = self.database.write_products()
        self.assertEqual(res, ['ogurci', 'banan', 'voda'])
        
    def test_write_klienti(self) :
        otv = self.database.write_klienti()
        self.assertEqual(res, ['Petr Nikolaevich', 'Dmitrii', 'Djonson'])
    
    def test_write_products_klienti(self) :
        otv = self.database.write_products_klienti('Petr Nikolaevich')
        self.assertEqual(res, ['banan', 2, 9012022]['voda', 1, 9012022])
    
    def test_zena_pokupki_za_vse_vreme(self) :
        otv = self.database.zena_pokupki_za_vse_vreme('Petr Nikolaevich')
        self.assertEqual(res, 21.89)
        
if __name__ == '__main__' :
    unittest.main()