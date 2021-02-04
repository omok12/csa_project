import pandas as pd
import matplotlib.pyplot as plt

#import csv and return dataframe with trades with csa
def import_clean_csv(path='./2020_q1.csv'):
    df = pd.read_csv(path).fillna(0)
    df_commission = df[df['CSA Commission'] != 0]
    return df_commission

#find sum of csa and groupby 
def csa_cost(df, aggregate_column):
    df['total_csa_cost'] = abs(df['Quantity']) * df['CSA Commission']
    grouped_sum = df.groupby(aggregate_column).sum()
    grouped_sum['portion_to_csa'] = grouped_sum['total_csa_cost'] / grouped_sum['Commission']
    return grouped_sum

#truncate df to show relevant columns
def trunc_df(df, columns=['Trans Net Amt', 'Commission', 'total_csa_cost', 'portion_to_csa']):
    return df[columns]

#make plots
def make_plot(df):
    df = df.sort_values(by='Commission', ascending=False)
    print(df[['Commission', 'total_csa_cost', 'portion_to_csa']].to_markdown())
    plt.bar(df.index, df['Commission'], width = .8, color = 'b', label='Total Commission Amount')
    plt.bar(df.index, df['total_csa_cost'], width = .5,  color = 'r', label = 'Total CSA Cost')
    plt.legend()
    plt.show()
