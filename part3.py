from helper import *

#Part 3: Summary of Trans Net Amt
##In aggregate, absolute value of each trans net amt
account_summary = CsaSummary('Account')
account_summary.run(['Total Abs Val Quantity', 'Total Abs Val Trans Net Amt', 'commission_trans', 'csa_trans', 'Commission', 'total_csa_cost', 'portion_to_csa'])

underlying_summary = CsaSummary('Underlying')
underlying_summary.run(['Total Abs Val Quantity', 'Total Abs Val Trans Net Amt', 'commission_trans', 'csa_trans', 'Commission', 'total_csa_cost', 'portion_to_csa'])
##Separated buy/sells
account_buysell_summary = CsaSummary(['Account', 'BuySell'])
account_buysell_summary.run(['Quantity', 'Trans Net Amt', 'commission_trans', 'csa_trans', 'Commission', 'total_csa_cost', 'portion_to_csa'])

underlying_buysell_summary = CsaSummary(['Underlying', 'BuySell'])
underlying_buysell_summary.run(['Quantity', 'Trans Net Amt', 'commission_trans', 'csa_trans', 'Commission', 'total_csa_cost', 'portion_to_csa'])

