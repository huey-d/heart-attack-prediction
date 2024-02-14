import unittest
import os
import pandas as pd
class Dataset(unittest.TestCase):
    
    def setUp(self, data_path: str = "data", file_path: str="raw\heart.csv"):
        self.df = pd.read_csv(os.path.join(data_path, file_path))
        self.assertTrue(os.path.isfile(os.path.join(data_path, file_path)))
        self.assertFalse(self.df.empty)
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()