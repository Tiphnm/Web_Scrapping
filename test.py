import os 
import unittest
from webscrap import Carpet

class Testing_my_webscrap(unittest.TestCase):
    def test_carpet_list(self):
        test_Carpet= Carpet()
        test_Carpet.name_carpet()
        self.assertTrue(len(test_Carpet.carpet_name_list) == 40)


if __name__ == '__main__':
    unittest.main(verbosity =0)

