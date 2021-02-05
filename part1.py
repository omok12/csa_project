from helper import *

#Part 1:  Provide a summary of CSA by Account and in aggregate that shows the dollar value assessed and the relative portion of total commissions that went to CSA.
account_summary = CsaSummary('Account')
account_summary.run(['Commission', 'total_csa_cost', 'portion_to_csa'], sort='Commission', plot=True)
