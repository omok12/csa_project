from helper import *

#Part 1:  Provide a summary of CSA by Account and in aggregate that shows the dollar value assessed and the relative portion of total commissions that went to CSA.
account_summary = CsaSummary('Account')
account_summary.run(['Commission', 'total_csa_cost', 'portion_to_csa'], plot=True)

#Part 2:  Provide a summary of Commissions and CSA by Underlying (Column Q).  This can be done in Aggregate and doesn't need to be done by account.   The Trans Net Amt Column is the total dollar value of the trade.  You can choose to include that in your analysis if it fits.
underlying_summary = CsaSummary('Underlying')
underlying_summary.run(['Commission', 'total_csa_cost', 'portion_to_csa'], plot=True)

#Part 3: Summary of Trans Net Amt
##In aggregate, absolute value of each trans net amt
account_summary.run(['Total Abs Val Quantity', 'Total Abs Val Trans Net Amt', 'commission_trans', 'csa_trans', 'Commission', 'total_csa_cost', 'portion_to_csa'])
underlying_summary.run(['Total Abs Val Quantity', 'Total Abs Val Trans Net Amt', 'commission_trans', 'csa_trans', 'Commission', 'total_csa_cost', 'portion_to_csa'])
##Separated buy/sells
account_buysell_summary = CsaSummary(['Account', 'BuySell'])
account_buysell_summary.run(['Quantity', 'Trans Net Amt', 'commission_trans', 'csa_trans', 'Commission', 'total_csa_cost', 'portion_to_csa'])

underlying_buysell_summary = CsaSummary(['Underlying', 'BuySell'])
underlying_buysell_summary.run(['Quantity', 'Trans Net Amt', 'commission_trans', 'csa_trans', 'Commission', 'total_csa_cost', 'portion_to_csa'])
