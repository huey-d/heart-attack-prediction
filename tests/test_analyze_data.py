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
        self.assertTrue(os.path.isfile("data/visual_plots/age_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/caa_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/chol_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/cp_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/exng_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/fbs_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/oldpeak_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/output_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/restecg_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/sex_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/slp_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/thalachh_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/thall_chart.png"))
        self.assertTrue(os.path.isfile("data/visual_plots/trtbps_chart.png"))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()