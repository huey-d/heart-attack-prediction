from zipfile import ZipFile
import pandas as pd
import plotly.express
from utils import util


def extract_data():
    file_name = r'heart-attack-analysis-prediction-dataset.zip'
    
    with ZipFile(file_name, 'r') as zip:
        zip.extractall('data')
        print('Done Extracting')

    

def read_data(heart_data: str = 'data\heart.csv'):
    heart_df = pd.read_csv(heart_data)

    

    print(heart_df.head()) #show 1st 5 cells of dataframe

    print(heart_df.info()) # show dataset information

    print(heart_df.isna().sum()) #show sum of missing values in columns

    print(heart_df.isna().sum().max()) # show sum of all missing values

    print(heart_df.output.value_counts()) #show value counts in output column
    
    return heart_df

def visualize_data(df):
    
    charts = []

    # for age_chart, 

    age_chart = plotly.express.histogram(df, x=df['age'], title='Age Chart', nbins=20, text_auto=True)
    age_chart.show() #show image
    # age_chart.write_image('plots/age_chart.png', engine="kaleido") #save image into directory


    sex_chart = plotly.express.histogram(df, x=df['sex'], title='Sex Chart', nbins=20, text_auto=True)
    # sex_chart.show() #show image
    sex_chart.write_image('plots/sex_chart.png', engine="kaleido") #save image into directory


    cp_chart = plotly.express.histogram(df, x=df['cp'], title='CP Chart', nbins=20, text_auto=True)
    # cp_chart.show() #show image
    cp_chart.write_image('plots/cp_chart.png', engine="kaleido") #save image into directory


    trtbps_sugar_chart = plotly.express.histogram(df, x=df['trtbps'], title='trtbps Chart', nbins=20, text_auto=True)
    # trtbps_sugar_chart.show() #show image
    trtbps_sugar_chart.write_image('plots/trtbps_sugar_chart.png', engine="kaleido") #save image into directory


    chol_chart = plotly.express.histogram(df, x=df['chol'], title='chol Chart', nbins=20, text_auto=True)
    # chol_chart.show() #show image
    chol_chart.write_image('plots/chol_chart.png', engine="kaleido") #save image into directory


    fbs_chart = plotly.express.histogram(df, x=df['fbs'], title='fbs Chart', nbins=20, text_auto=True)
    # fbs_chart.show() #show image
    fbs_chart.write_image('plots/fbs_chart.png', engine="kaleido") #save image into directory


    restecg_chart = plotly.express.histogram(df, x=df['restecg'], title='restecg Chart', nbins=20, text_auto=True)
    # restecg_chart.show() #show image
    restecg_chart.write_image('plots/restecg_chart.png', engine="kaleido") #save image into directory


    thalachh_chart = plotly.express.histogram(df, x=df['thalachh'], title='thalachh Chart', nbins=20, text_auto=True)
    # thalachh_chart.show() #show image
    thalachh_chart.write_image('plots/thalachh_chart.png', engine="kaleido") #save image into directory


    exng_chart = plotly.express.histogram(df, x=df['exng'], title='exng Chart', nbins=20, text_auto=True)
    # exng_chart.show() #show image
    exng_chart.write_image('plots/exng_chart.png', engine="kaleido") #save image into directory


    oldpeak_chart = plotly.express.histogram(df, x=df['oldpeak'], title='oldpeak Chart', nbins=20, text_auto=True)
    # oldpeak_chart.show() #show image
    oldpeak_chart.write_image('plots/oldpeak_chart.png', engine="kaleido") #save image into directory


    slp_chart = plotly.express.histogram(df, x=df['slp'], title='slp Chart', nbins=20, text_auto=True)
    # slp_chart.show() #show image
    slp_chart.write_image('plots/slp_chart.png', engine="kaleido") #save image into directory


    label_chart = plotly.express.histogram(df, x='quality', title='Wine Quality Chart', color='quality', text_auto=True)
    # label_chart.show() #show image
    label_chart.write_image('plots/quality_chart.png', engine="kaleido") #save image into directory

    label_chart = plotly.express.histogram(df, x='quality', title='Wine Quality Chart', color='quality', text_auto=True)
    # label_chart.show() #show image
    label_chart.write_image('plots/quality_chart.png', engine="kaleido") #save image into directory
    
    label_chart = plotly.express.histogram(df, x='quality', title='Wine Quality Chart', color='quality', text_auto=True)
    # label_chart.show() #show image
    label_chart.write_image('plots/quality_chart.png', engine="kaleido") #save image into directory
    
    label_chart = plotly.express.histogram(df, x='quality', title='Wine Quality Chart', color='quality', text_auto=True)
    # label_chart.show() #show image
    label_chart.write_image('plots/quality_chart.png', engine="kaleido") #save image into directory
    
    label_chart = plotly.express.histogram(df, x='quality', title='Wine Quality Chart', color='quality', text_auto=True)
    # label_chart.show() #show image
    label_chart.write_image('plots/quality_chart.png', engine="kaleido") #save image into directory








if __name__ == '__main__':
    util.make_dirs()
    extract_data() 
    new_data = read_data()
    # visualize_data(new_data)