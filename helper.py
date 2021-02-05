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
        df['Total Abs Val Quantity'] = abs(df['Quantity'])
        df['Total Abs Val Trans Net Amt'] = abs(df['Trans Net Amt'])
        grouped_sum = df.groupby(self.aggregate_column).sum()
        grouped_sum['portion_to_csa'] = grouped_sum['total_csa_cost'] / grouped_sum['Commission']
        grouped_sum['commission_trans'] = grouped_sum['Commission'] / grouped_sum['Total Abs Val Trans Net Amt']
        grouped_sum['csa_trans'] = grouped_sum['total_csa_cost'] / grouped_sum['Total Abs Val Trans Net Amt']
        return grouped_sum

    def to_markdown(self, df):
        print(df.to_markdown())

    def make_plot(self, df):
        plt.bar(df.index, df['Commission'], width = .8, color = 'b', label='Total Commission Amount')
        plt.bar(df.index, df['total_csa_cost'], width = .5,  color = 'r', label = 'Total CSA Cost')
        plt.xticks(rotation=90)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f'./img/{self.aggregate_column}_csa_summary')
        plt.show()

    def style_df(self, df):
        percentage = ['portion_to_csa', 'commission_trans', 'csa_trans']
        for c in percentage:
            df[c] = (df[c]*100).apply('{:,.2f}%'.format)
        dollar = ['total_csa_cost', 'Total Abs Val Trans Net Amt', 'Trans Net Amt', 'Commission', 'CSA Commission']
        for c in dollar:
            df[c] = (df[c]/100).apply('${0:,.2f}'.format)
        return df

    def run(self, columns,sort=False, plot=False):
        df = self.csa_cost(self.import_clean_csv())
        if sort:
            df = df.sort_values(by=sort, ascending=False)
        if plot:
            self.make_plot(df[columns])
        df = self.style_df(df)
        self.to_markdown(df[columns])
