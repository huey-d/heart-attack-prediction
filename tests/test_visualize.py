import pandas as pd
import os
import unittest

class VisualizeData(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_visualize_data(self):
        self.assertTrue(os.path.isfile("reports/figures/age.png"))
        self.assertTrue(os.path.isfile("reports/figures/caa.png"))
        self.assertTrue(os.path.isfile("reports/figures/chol.png"))
        self.assertTrue(os.path.isfile("reports/figures/cp.png"))
        self.assertTrue(os.path.isfile("reports/figures/exng.png"))
        self.assertTrue(os.path.isfile("reports/figures/fbs.png"))
        self.assertTrue(os.path.isfile("reports/figures/oldpeak.png"))
        self.assertTrue(os.path.isfile("reports/figures/output.png"))
        self.assertTrue(os.path.isfile("reports/figures/restecg.png"))
        self.assertTrue(os.path.isfile("reports/figures/sex.png"))
        self.assertTrue(os.path.isfile("reports/figures/slp.png"))
        self.assertTrue(os.path.isfile("reports/figures/thalachh.png"))
        self.assertTrue(os.path.isfile("reports/figures/thall.png"))
        self.assertTrue(os.path.isfile("reports/figures/trtbps.png"))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()