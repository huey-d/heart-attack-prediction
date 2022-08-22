import os


def make_dirs():
    data_path = "data/"
    output_path = "output/"
    model_file = "final_model/"
        
    for _ in [data_path, output_path, model_file]:
        if not os.path.exists(_):
            os.mkdir(_)


