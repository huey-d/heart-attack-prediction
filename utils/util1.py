import os
from zipfile import ZipFile

def directories(testing: str = "no"):
    
    if testing == 'no':
        data_path = "data/"
        dataset_path = "data/datasets/"
        model_output = "data/model_output/"
        visuals_path = "data/visual_plots/"



        for _ in [data_path, dataset_path, model_output, visuals_path]:
            if not os.path.exists(_):
                os.mkdir(_)
    
    # elif testing == 'yes':
    #     test_path = "test/"
    #     test_data_path = "test/data/"
    #     test_dataset_path = "test/data/datasets/"
    #     test_model_output = "test/data/model_output/"
    #     test_visuals_path = "test/data/visual_plots/"
    #     for _ in [test_path, test_data_path, test_dataset_path, test_model_output, test_visuals_path]:
    #         if not os.path.exists(_):
    #             os.mkdir(_)


if __name__ == '__main__':
    directories()