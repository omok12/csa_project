from helper import *

#Part 1:  Provide a summary of CSA by Account and in aggregate that shows the dollar value assessed and the relative portion of total commissions that went to CSA.
account_summary = CsaSummary('Account')
account_summary.run()
#account 26 had higher commissions than other accounts
#make_plot(df[df.index != 'account_26'])

#Part 2:  Provide a summary of Commissions and CSA by Underlying (Column Q).  This can be done in Aggregate and doesn't need to be done by account.   The Trans Net Amt Column is the total dollar value of the trade.  You can choose to include that in your analysis if it fits.
underlying_summary = CsaSummary('Underlying')
underlying_summary.run()

#df3 = csa_cost(import_clean_csv(), ['Account', 'Broker Code', 'Underlying', 'BuySell'])
test_summary = CsaSummary(['Account', 'BuySell'])
test_summary.run()
