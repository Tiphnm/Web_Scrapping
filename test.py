import os 
import unittest
from webscrap import Carpet
from webscrap import Mirror

class Testing_my_webscrap(unittest.TestCase):
    def test_carpet_list(self):
        test_Carpet= Carpet()
        test_Carpet.name_carpet()
        self.assertTrue(len(test_Carpet.carpet_name_list) == 40)
    
    def test_carpet_price_list(self): 
        test_Carpet= Carpet()
        test_Carpet.price_carpet()
        self.assertTrue(len(test_Carpet.carpet_price_list) == 40)

    def test_mirror_list(self):
        test_Mirror= Mirror()
        test_Mirror.name_mirror()
        self.assertTrue(len(test_Mirror.mirror_name_list) == 40)

    def test_mirror_price_list(self):
        test_Mirror= Mirror()
        test_Mirror.price_mirror()
        self.assertTrue(len(test_Mirror.mirror_price_list) == 40)

if __name__ == '__main__':
    unittest.main(verbosity =0)

