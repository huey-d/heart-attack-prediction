import unittest
import utils.util
import os
import shutil

class TestDirectories(unittest.TestCase):
    
    def setUp(self):
        # self.function = utils.util1.directories()
        pass

    def test_make_dirs(self):
        self.assertTrue(os.path.exists("data"))
        self.assertTrue(os.path.exists("data/datasets"))
        self.assertTrue(os.path.exists("data/visual_plots"))
        self.assertTrue(os.path.exists("data"))
        self.assertTrue(os.path.exists("data/datasets"))
        self.assertTrue(os.path.exists("data/visual_plots"))
        self.assertTrue(os.path.exists("data"))
        self.assertTrue(os.path.exists("data/datasets"))
        self.assertTrue(os.path.exists("data/visual_plots"))

    def tearDown(self):
        pass
    

if __name__ == '__main__':
    unittest.main()