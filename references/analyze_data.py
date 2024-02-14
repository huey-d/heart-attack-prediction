import pandas as pd
import os
import sklearn.model_selection

def read_data(data_path: str = "data", file_path: str = "raw/heart.csv"):
    heart_df = pd.read_csv(os.path.join(data_path, file_path))
    
    print(heart_df.head())  # show 1st 5 cells of dataframe
    print(heart_df.info())  # show dataset information
    print(heart_df.isna().sum())  # show sum of missing values in columns
    print(heart_df.isna().sum().max())  # show sum of all missing values
    print(heart_df.output.value_counts())  # show value counts in output column
    return heart_df

# def process_data(data_path: str = "data", file_path: str = "raw/heart.csv"):
#     df = pd.read_csv(os.path.join(data_path, file_path))
    
#     X = df.drop(columns=['output'], axis=1)
#     y = df['output']

#     X_train, X_test, y_train, y_test  = sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

#     X_train.to_csv("data/processed")
#     X_test.to_csv("data/processed")
#     y_train.to_csv("data/processed")
#     y_test.to_csv("data/processed")


if __name__ == '__main__':
    new_data = read_data()
    # process_data()