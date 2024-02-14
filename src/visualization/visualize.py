import plotly.express
import pandas as pd
import os

def visualize_data(data_path: str = "data", file_path: str = "raw/heart.csv"):

    df = pd.read_csv(os.path.join(data_path, file_path))

    age = plotly.express.histogram(df, x=df['age'], title='Age Chart', nbins=20, text_auto=True)
    # age.show()
    age.write_image('reports/figures/age.png', engine="kaleido")

    sex = plotly.express.histogram(df, x=df['sex'], title='Sex Chart', nbins=20, text_auto=True)
    # sex.show()
    sex.write_image('reports/figures/sex.png', engine="kaleido")

    cp = plotly.express.histogram(df, x=df['cp'], title='CP Chart', nbins=20, text_auto=True)
    # cp.show() 
    cp.write_image('reports/figures/cp.png', engine="kaleido")

    trtbps = plotly.express.histogram(df, x=df['trtbps'], title='trtbps Chart', nbins=20, text_auto=True)
    # trtbps.show()
    trtbps.write_image('reports/figures/trtbps.png', engine="kaleido")

    chol = plotly.express.histogram(df, x=df['chol'], title='chol Chart', nbins=20, text_auto=True)
    # chol.show()
    chol.write_image('reports/figures/chol.png', engine="kaleido")

    fbs = plotly.express.histogram(df, x=df['fbs'], title='fbs Chart', nbins=20, text_auto=True)
    # fbs.show()
    fbs.write_image('reports/figures/fbs.png', engine="kaleido")

    restecg = plotly.express.histogram(df, x=df['restecg'], title='restecg Chart', nbins=20, text_auto=True)
    # restecg.show()
    restecg.write_image('reports/figures/restecg.png', engine="kaleido")

    thalachh = plotly.express.histogram(df, x=df['thalachh'], title='thalachh Chart', nbins=20, text_auto=True)
    # thalachh.show() 
    thalachh.write_image('reports/figures/thalachh.png', engine="kaleido")

    exng = plotly.express.histogram(df, x=df['exng'], title='exng Chart', nbins=20, text_auto=True)
    # exng.show()
    exng.write_image('reports/figures/exng.png', engine="kaleido")

    oldpeak = plotly.express.histogram(df, x=df['oldpeak'], title='oldpeak Chart', nbins=20, text_auto=True)
    # oldpeak.show()
    oldpeak.write_image('reports/figures/oldpeak.png', engine="kaleido")

    slp = plotly.express.histogram(df, x=df['slp'], title='slp Chart', nbins=20, text_auto=True)
    # slp.show()
    slp.write_image('reports/figures/slp.png', engine="kaleido")

    caa = plotly.express.histogram(df, x=df['caa'], title='caa Chart', nbins=20, text_auto=True)
    # caa.show() 
    caa.write_image('reports/figures/caa.png', engine="kaleido")

    thall = plotly.express.histogram(df, x=df['thall'], title='thall Chart', nbins=20, text_auto=True)
    # thall.show()
    thall.write_image('reports/figures/thall.png', engine="kaleido")

    output = plotly.express.histogram(df, x=df['output'], title='output Chart', nbins=20, text_auto=True)
    # output.show()
    output.write_image('reports/figures/output.png', engine="kaleido")

if __name__ == '__main__':
    visualize_data()