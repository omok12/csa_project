from helper import *

#Part 1:  Provide a summary of CSA by Account and in aggregate that shows the dollar value assessed and the relative portion of total commissions that went to CSA.
df = csa_cost(import_clean_csv(), 'Account')
print(trunc_df(df))
#make_plot(df)
#account 26 had higher commissions than other accounts
make_plot(df[df.index != 'account_26'])

#Part 2:  Provide a summary of Commissions and CSA by Underlying (Column Q).  This can be done in Aggregate and doesn't need to be done by account.   The Trans Net Amt Column is the total dollar value of the trade.  You can choose to include that in your analysis if it fits.
df2 = csa_cost(import_clean_csv(), 'Underlying')
print(trunc_df(df2))
make_plot(df2)

df3 = csa_cost(import_clean_csv(), ['Account', 'Broker Code', 'Underlying', 'BuySell'])
print(trunc_df(df3))
