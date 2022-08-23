import pandas as pd
import plotly.express

def read_data(heart_data: str = 'data\datasets\heart.csv'):
    heart_df = pd.read_csv(heart_data)
    
    print(heart_df.head())  # show 1st 5 cells of dataframe
    print(heart_df.info())  # show dataset information
    print(heart_df.isna().sum())  # show sum of missing values in columns
    print(heart_df.isna().sum().max())  # show sum of all missing values
    print(heart_df.output.value_counts())  # show value counts in output column
    return heart_df

def visualize_data(df):

    age = plotly.express.histogram(df, x=df['age'], title='Age Chart', nbins=20, text_auto=True)
    # age.show()
    age.write_image('data/visual_plots/age.png', engine="kaleido")

    sex = plotly.express.histogram(df, x=df['sex'], title='Sex Chart', nbins=20, text_auto=True)
    # sex.show()
    sex.write_image('data/visual_plots/sex.png', engine="kaleido")

    cp = plotly.express.histogram(df, x=df['cp'], title='CP Chart', nbins=20, text_auto=True)
    # cp.show() 
    cp.write_image('data/visual_plots/cp.png', engine="kaleido")

    trtbps = plotly.express.histogram(df, x=df['trtbps'], title='trtbps Chart', nbins=20, text_auto=True)
    # trtbps.show()
    trtbps.write_image('data/visual_plots/trtbps.png', engine="kaleido")

    chol = plotly.express.histogram(df, x=df['chol'], title='chol Chart', nbins=20, text_auto=True)
    # chol.show()
    chol.write_image('data/visual_plots/chol.png', engine="kaleido")

    fbs = plotly.express.histogram(df, x=df['fbs'], title='fbs Chart', nbins=20, text_auto=True)
    # fbs.show()
    fbs.write_image('data/visual_plots/fbs.png', engine="kaleido")

    restecg = plotly.express.histogram(df, x=df['restecg'], title='restecg Chart', nbins=20, text_auto=True)
    # restecg.show()
    restecg.write_image('data/visual_plots/restecg.png', engine="kaleido")

    thalachh = plotly.express.histogram(df, x=df['thalachh'], title='thalachh Chart', nbins=20, text_auto=True)
    # thalachh.show() 
    thalachh.write_image('data/visual_plots/thalachh.png', engine="kaleido")

    exng = plotly.express.histogram(df, x=df['exng'], title='exng Chart', nbins=20, text_auto=True)
    # exng.show()
    exng.write_image('data/visual_plots/exng.png', engine="kaleido")

    oldpeak = plotly.express.histogram(df, x=df['oldpeak'], title='oldpeak Chart', nbins=20, text_auto=True)
    # oldpeak.show()
    oldpeak.write_image('data/visual_plots/oldpeak.png', engine="kaleido")

    slp = plotly.express.histogram(df, x=df['slp'], title='slp Chart', nbins=20, text_auto=True)
    # slp.show()
    slp.write_image('data/visual_plots/slp.png', engine="kaleido")

    caa = plotly.express.histogram(df, x=df['caa'], title='caa Chart', nbins=20, text_auto=True)
    # caa.show() 
    caa.write_image('data/visual_plots/caa.png', engine="kaleido")

    thall = plotly.express.histogram(df, x=df['thall'], title='thall Chart', nbins=20, text_auto=True)
    # thall.show()
    thall.write_image('data/visual_plots/thall.png', engine="kaleido")

    output = plotly.express.histogram(df, x=df['output'], title='output Chart', nbins=20, text_auto=True)
    # output.show()
    output.write_image('data/visual_plots/output.png', engine="kaleido")

if __name__ == '__main__':
    new_data = read_data()
    visualize_data(new_data)
