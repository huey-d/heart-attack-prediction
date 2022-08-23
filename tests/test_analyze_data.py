import unittest
import os
import pandas as pd
class Dataset(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.read_csv("data\datasets\heart.csv")
        self.assertTrue(os.path.isfile("data\datasets\heart.csv"))
    
    def test_read_data(self):
        df = pd.read_csv("data\datasets\heart.csv")
        self.assertFalse(df.empty)
    
    def test_visualize_data(self):
        self.assertTrue(os.path.isfile("data/visual_plots/age.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/caa.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/chol.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/cp.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/exng.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/fbs.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/oldpeak.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/output.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/restecg.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/sex.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/slp.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/thalachh.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/thall.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/trtbps.png"))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()