import unittest
import utils.util
import os
import shutil

class TestDirectories(unittest.TestCase):
    
    def setUp(self):
        # self.function = utils.util1.directories()
        pass

    def test_make_dirs(self):
        utils_path = "utils/"
        data_ext = "data/external/"
        data_int = "data/interim/"
        data_proc = "data/processed/"
        data_raw = "data/raw/"
        model_path = "models/"
        references_path = "references/"
        reports_path = "reports/figures/"
        test_path = "tests/"
        src_data = "src/data"
        src_features = "src/features"
        src_models = "src/models"
        src_visuals = "src/visualization"

        self.assertTrue(os.path.exists(utils_path))
        self.assertTrue(os.path.exists(data_ext))
        self.assertTrue(os.path.exists(data_int))
        self.assertTrue(os.path.exists(data_proc))
        self.assertTrue(os.path.exists(data_raw))
        self.assertTrue(os.path.exists(model_path))
        self.assertTrue(os.path.exists(references_path))
        self.assertTrue(os.path.exists(reports_path))
        self.assertTrue(os.path.exists(test_path))
        self.assertTrue(os.path.exists(src_data))
        self.assertTrue(os.path.exists(src_features))
        self.assertTrue(os.path.exists(src_models))
        self.assertTrue(os.path.exists(src_visuals))

    def tearDown(self):
        pass
    

if __name__ == '__main__':
    unittest.main()