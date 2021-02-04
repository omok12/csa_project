import pandas as pd
import matplotlib.pyplot as plt

class CsaSummary:
    def __init__(self, aggregate_column, path='./2020_q1.csv'):
        self.path = path
        self.aggregate_column = aggregate_column

    #import csv and return dataframe with trades with csa
    def import_clean_csv(self):
        df = pd.read_csv(self.path).fillna(0)
        df_commission = df[df['CSA Commission'] != 0]
        return df_commission

    #find sum of csa and groupby 
    def csa_cost(self, df, sort='Commission'):
        df['total_csa_cost'] = abs(df['Quantity']) * df['CSA Commission']
        grouped_sum = df.groupby(self.aggregate_column).sum()
        grouped_sum['portion_to_csa'] = ((grouped_sum['total_csa_cost'] / grouped_sum['Commission'])* 100).map('{}%'.format)
        grouped_sum = grouped_sum.sort_values(by=sort, ascending=False)
        return grouped_sum

    #truncate df to show relevant columns
    def trunc_df(self, df, columns=['Trans Net Amt', 'Commission', 'total_csa_cost', 'portion_to_csa']):
        return df[columns]

    #to_markdown
    def to_markdown(self, df):
        print(df[['Commission', 'total_csa_cost', 'portion_to_csa']].to_markdown())

    #make plots
    def make_plot(self, df):
        plt.bar(df.index, df['Commission'], width = .8, color = 'b', label='Total Commission Amount')
        plt.bar(df.index, df['total_csa_cost'], width = .5,  color = 'r', label = 'Total CSA Cost')
        plt.legend()
        plt.savefig(f'./img/{self.aggregate_column}_csa_summary')
        plt.show()

    def run(self, trunc=False):
        df = self.csa_cost(self.import_clean_csv())
        if type(self.aggregate_column) is str:
            self.to_markdown(df)
            self.make_plot(df)
        else:
            self.to_markdown(df)
