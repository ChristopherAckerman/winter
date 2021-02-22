import numpy as np
import pandas as pd
import statsmodels.api as sm
import scipy.io
from statsmodels.sandbox.regression.gmm import IV2SLS


def load_matlab_data(filename='Schooling.mat'):
    matlab_data = scipy.io.loadmat(filename)
    df = pd.DataFrame(
        columns=[data_field for data_field in matlab_data.keys() if data_field[0] != '_']
        )
    df = df.drop('ans', axis='columns')
    df = df.drop('None', axis='columns')
    for column in df.columns:
        print(column)
        df[column] = matlab_data[column].flatten()
    return df


def run_OLS(dataframe, filename=False):
    X = df[['educ', 'black', 'age', 'agesquared']]
    Y = df[['lwage']]
    X = sm.add_constant(X)
    lm = sm.OLS(Y, X)
    results = lm.fit()
    print(results.summary())
    if filename:
        with open(filename, 'w') as text_file:
            print(f'{results.summary().as_latex()}', file=text_file)


def run_IV(dataframe, instruments, filename=False):
    X = df[['educ', 'black', 'age', 'agesquared']]
    Z = df[instruments]
    Y = df[['lwage']]
    X = sm.add_constant(X)
    Z = sm.add_constant(Z)
    iv = IV2SLS(Y, X, Z)
    results = iv.fit()
    print(results.summary())
    if filename:
        with open(filename, 'w') as text_file:
            print(f'{results.summary().as_latex()}', file=text_file)


if __name__ == '__main__':
    df = load_matlab_data()
    run_OLS(dataframe=df, filename='ols.tex')
    run_IV(dataframe=df, instruments=['nearc4', 'black', 'age', 'agesquared'],
           filename='iv1.tex')
    run_IV(dataframe=df, instruments=['nearc2', 'nearc4', 'black', 'age', 'agesquared'],
           filename='iv2.tex')




