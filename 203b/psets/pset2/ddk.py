import numpy as np
import os
import pandas as pd
import scipy.io
import statsmodels.api as sm


def load_matlab_data(filename='DDKData.mat'):
    matlab_data = scipy.io.loadmat(filename)
    df = pd.DataFrame(
        columns=[data_field for data_field in matlab_data.keys() if data_field[0] != '_']
        )
    for column in df.columns:
        df[column] = matlab_data[column].flatten()
    return df


def drop_missing_observations(dataframe, obs_to_check=['girl', 'std_mark', 'totalscore', 'tracking']):
    original_nObs = dataframe.shape[0]
    df = dataframe.dropna(subset=obs_to_check)
    print(f'We dropped {original_nObs - df.shape[0]} observations.')
    return df


def calculate_summary_statistics(dataframe, filename=False):
    num_boys = dataframe.shape[0] - dataframe.girl.sum() 
    num_tracking = dataframe.tracking.sum()
    original_score = dataframe.std_mark.mean() 
    unique_schools = len(dataframe.schoolid.unique())
    if filename:
        with open(filename, 'w') as text_file:
            print(f'Our dataset contains {num_boys} boys. \
                    {num_tracking} students were assigned to tracking schools. \
                    The average baseline original score was {original_score}, \
                    and our dataset contains {unique_schools} unique schools.',
                  file=text_file)


def prepare_datasets(dataframe):
    dataframe['const'] = 1
    girls = dataframe[dataframe.girl == 1]
    boys = dataframe[dataframe.girl == 0]
    dataframe['boy'] = pd.get_dummies(dataframe['girl'])[0.0]
    dataframe['treated_boy'] = dataframe['tracking'] * dataframe['boy']
    dataframe['treated_girl'] = dataframe['tracking'] * dataframe['girl']
    top = dataframe[dataframe['tophalf'] == 1]
    bottom = dataframe[dataframe['bottomhalf'] == 1]
    return dataframe, girls, boys, top, bottom

    
def calculate_ATE(dataframe, outcome, exog, filename=False):
    reg = sm.OLS(endog=dataframe[outcome],
                exog=dataframe[exog]
                ).fit()
    if filename:
        with open(filename, 'w') as text_file:
            print(f'{reg.summary().as_latex()}', file=text_file)
    else:
        print(reg.summary())


if __name__ == '__main__':
    os.chdir('/home/chris/files/school/ucla/first_year/winter/203b/psets/pset1')
    df = load_matlab_data()
    df = drop_missing_observations(df)
    calculate_summary_statistics(df, filename='summary_statistics.tex')
    complete_dataset, girls, boys, top, bottom = prepare_datasets(df)
    girls_spec = [girls, 'totalscore', ['const', 'tracking'], 'girls.tex']
    boys_spec = [boys, 'totalscore', ['const', 'tracking'], 'boys.tex']
    all_spec = [complete_dataset, 'totalscore', ['const', 'girl', 'treated_boy', 'treated_girl'], 'all.tex']
    top_spec = [top, 'totalscore', ['const', 'tracking'], 'top.tex']
    bottom_spec = [bottom, 'totalscore', ['const', 'tracking'], 'bottom.tex']
    specifications = [girls_spec, boys_spec, all_spec, top_spec, bottom_spec]
    for specification in specifications:
        calculate_ATE(*specification)
    
reg_HC1 = sm.OLS(endog=girls['totalscore'],
                 exog=girls[['const', 'tracking']]
                 ).fit()

with open('../pset2/nonrobust.tex', 'w') as text_file:
    print(f'{reg_HC1.summary().as_latex()}', file=text_file)

with open('../pset2/hc1.tex', 'w') as text_file:
    print(f'{reg_HC1.get_robustcov_results().summary().as_latex()}', file=text_file)

hc2 = reg_HC1.get_robustcov_results(cov_type='HC2')
with open('../pset2/hc2.tex', 'w') as text_file:
    print(f'{hc2.summary().as_latex()}', file=text_file)


complete_dataset['top_tracking'] = complete_dataset['tophalf']* complete_dataset['tracking']
complete_dataset.head(3)
    
top_ate_test = sm.OLS(endog=complete_dataset['totalscore'],
                 exog=complete_dataset[['const', 'tracking', 'tophalf', 'top_tracking']]
                 ).fit()

with open('../pset2/top_ate_test.tex', 'w') as text_file:
    print(f'{top_ate_test.summary().as_latex()}', file=text_file)
