import os
import pickle

script_dir = os.path.dirname('deploy_xgboost.pkl')

from pathlib import Path

data_folder = Path("backend")
file_to_open = data_folder / "deploy_xgboost.pkl"

print(data_folder)
print(file_to_open)

with open(file_to_open, 'rb') as f:
    load_model = pickle.load(f)

print(load_model)