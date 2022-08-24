import pandas as pd
import os

def read_data(data_path: str = "data", file_path: str = "raw/heart.csv"):
    heart_df = pd.read_csv(os.path.join(data_path, file_path))
    
    print(heart_df.head())  # show 1st 5 cells of dataframe
    print(heart_df.info())  # show dataset information
    print(heart_df.isna().sum())  # show sum of missing values in columns
    print(heart_df.isna().sum().max())  # show sum of all missing values
    print(heart_df.output.value_counts())  # show value counts in output column
    return heart_df



if __name__ == '__main__':
    new_data = read_data()