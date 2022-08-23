from zipfile import ZipFile
import pandas as pd
import plotly.express
from utils import util
import kaggle

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

    age_chart = plotly.express.histogram(df, x=df['age'], title='Age Chart', nbins=20, text_auto=True)
    # age_chart.show() #show image
    age_chart.write_image('output/age_chart.png', engine="kaleido") #save image into directory


    sex_chart = plotly.express.histogram(df, x=df['sex'], title='Sex Chart', nbins=20, text_auto=True)
    # sex_chart.show() #show image
    sex_chart.write_image('output/sex_chart.png', engine="kaleido") #save image into directory


    cp_chart = plotly.express.histogram(df, x=df['cp'], title='CP Chart', nbins=20, text_auto=True)
    # cp_chart.show() #show image
    cp_chart.write_image('output/cp_chart.png', engine="kaleido") #save image into directory


    trtbps_chart = plotly.express.histogram(df, x=df['trtbps'], title='trtbps Chart', nbins=20, text_auto=True)
    # trtbps_chart.show() #show image
    trtbps_chart.write_image('output/trtbps_chart.png', engine="kaleido") #save image into directory


    chol_chart = plotly.express.histogram(df, x=df['chol'], title='chol Chart', nbins=20, text_auto=True)
    # chol_chart.show() #show image
    chol_chart.write_image('output/chol_chart.png', engine="kaleido") #save image into directory


    fbs_chart = plotly.express.histogram(df, x=df['fbs'], title='fbs Chart', nbins=20, text_auto=True)
    # fbs_chart.show() #show image
    fbs_chart.write_image('output/fbs_chart.png', engine="kaleido") #save image into directory


    restecg_chart = plotly.express.histogram(df, x=df['restecg'], title='restecg Chart', nbins=20, text_auto=True)
    # restecg_chart.show() #show image
    restecg_chart.write_image('output/restecg_chart.png', engine="kaleido") #save image into directory


    thalachh_chart = plotly.express.histogram(df, x=df['thalachh'], title='thalachh Chart', nbins=20, text_auto=True)
    # thalachh_chart.show() #show image
    thalachh_chart.write_image('output/thalachh_chart.png', engine="kaleido") #save image into directory


    exng_chart = plotly.express.histogram(df, x=df['exng'], title='exng Chart', nbins=20, text_auto=True)
    # exng_chart.show() #show image
    exng_chart.write_image('output/exng_chart.png', engine="kaleido") #save image into directory


    oldpeak_chart = plotly.express.histogram(df, x=df['oldpeak'], title='oldpeak Chart', nbins=20, text_auto=True)
    # oldpeak_chart.show() #show image
    oldpeak_chart.write_image('output/oldpeak_chart.png', engine="kaleido") #save image into directory


    slp_chart = plotly.express.histogram(df, x=df['slp'], title='slp Chart', nbins=20, text_auto=True)
    # slp_chart.show() #show image
    slp_chart.write_image('output/slp_chart.png', engine="kaleido") #save image into directory


    caa_chart = plotly.express.histogram(df, x=df['caa'], title='caa Chart', nbins=20, text_auto=True)
    # caa_chart.show() #show image
    caa_chart.write_image('output/caa_chart.png', engine="kaleido") #save image into directory


    thall_chart = plotly.express.histogram(df, x=df['thall'], title='thall Chart', nbins=20, text_auto=True)
    # thall_chart.show() #show image
    thall_chart.write_image('output/thall_chart.png', engine="kaleido") #save image into directory


    output_chart = plotly.express.histogram(df, x=df['output'], title='output Chart', nbins=20, text_auto=True)
    # output_chart.show() #show image
    output_chart.write_image('output/output_chart.png', engine="kaleido") #save image into directory



if __name__ == '__main__':
    util.make_dirs()
    extract_data() 
    new_data = read_data()
    visualize_data(new_data)