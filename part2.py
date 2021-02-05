from helper import *

#Part 2:  Provide a summary of Commissions and CSA by Underlying (Column Q).  This can be done in Aggregate and doesn't need to be done by account.   The Trans Net Amt Column is the total dollar value of the trade.  You can choose to include that in your analysis if it fits.
underlying_summary = CsaSummary('Underlying')
underlying_summary.run(['Commission', 'total_csa_cost', 'portion_to_csa'], plot=True)

