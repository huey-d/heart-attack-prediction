import os


def make_dirs():
    data_path = "data/"
    output_path = "output/"
    model_file = "model_file/"
        
    for _ in [data_path, output_path, model_file]:
        if not os.path.exists(_):
            os.mkdir(_)