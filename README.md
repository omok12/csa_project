# Part 1:  Provide a summary of CSA by Account and in aggregate that shows the dollar value assessed and the relative portion of total commissions that went to CSA.

| Account    |   Commission |   total_csa_cost | portion_to_csa   |
|:-----------|-------------:|-----------------:|:-----------------|
| account_26 |       333928 |           250446 | 75.0%            |
| account_12 |         2080 |             1560 | 75.0%            |
| account_25 |         1484 |             1113 | 75.0%            |
| account_13 |          984 |              738 | 75.0%            |
| account_28 |          964 |              723 | 75.0%            |
| account_30 |          908 |              681 | 75.0%            |
| account_14 |          892 |              669 | 75.0%            |
| account_8  |          808 |              606 | 75.0%            |
| account_11 |          564 |              423 | 75.0%            |
| account_31 |          448 |              336 | 75.0%            |
| account_22 |          408 |              306 | 75.0%            |
| account_32 |          408 |              306 | 75.0%            |
| account_23 |          404 |              303 | 75.0%            |
| account_27 |          300 |              225 | 75.0%            |
| account_29 |          220 |              165 | 75.0%            |
| account_10 |          212 |              159 | 75.0%            |

![Summary by Account](./img/Account_csa_summary.png)

![Summary by Account w/o account_26](./img/account_csa_summary_no_26.png)

# Part 2:  Provide a summary of Commissions and CSA by Underlying (Column Q).  This can be done in Aggregate and doesn't need to be done by account. 

![Summary by Underlying](./img/Underlying_csa_summary.png)

| Underlying   |   Commission |   total_csa_cost | portion_to_csa   |
|:-------------|-------------:|-----------------:|:-----------------|
| SPX          |       345012 |           258759 | 75.0%            |

# Part 3: Summary of Trans Net Amt
## In Aggregate
| Account    |   Total Abs Val Quantity |   Total Abs Val Trans Net Amt | commission_trans   | csa_trans   |   Commission |   total_csa_cost | portion_to_csa   |
|:-----------|-------------------------:|------------------------------:|:-------------------|:------------|-------------:|-----------------:|:-----------------|
| account_26 |                    83482 |                   2.7466e+08  | 0.12%              | 0.09%       |       333928 |           250446 | 75.0%            |
| account_12 |                      520 |                   1.66928e+06 | 0.12%              | 0.09%       |         2080 |             1560 | 75.0%            |
| account_25 |                      371 |                   2.28159e+06 | 0.07%              | 0.05%       |         1484 |             1113 | 75.0%            |
| account_13 |                      246 |                   1.56447e+06 | 0.06%              | 0.05%       |          984 |              738 | 75.0%            |
| account_28 |                      241 |              800553           | 0.12%              | 0.09%       |          964 |              723 | 75.0%            |
| account_30 |                      227 |              879948           | 0.1%               | 0.08%       |          908 |              681 | 75.0%            |
| account_14 |                      223 |                   1.18687e+06 | 0.08%              | 0.06%       |          892 |              669 | 75.0%            |
| account_8  |                      202 |                   1.26516e+06 | 0.06%              | 0.05%       |          808 |              606 | 75.0%            |
| account_11 |                      141 |              484247           | 0.12%              | 0.09%       |          564 |              423 | 75.0%            |
| account_31 |                      112 |              437847           | 0.1%               | 0.08%       |          448 |              336 | 75.0%            |
| account_22 |                      102 |              339907           | 0.12%              | 0.09%       |          408 |              306 | 75.0%            |
| account_32 |                      102 |              392418           | 0.1%               | 0.08%       |          408 |              306 | 75.0%            |
| account_23 |                      101 |              337793           | 0.12%              | 0.09%       |          404 |              303 | 75.0%            |
| account_27 |                       75 |               56282.3         | 0.53%              | 0.4%        |          300 |              225 | 75.0%            |
| account_29 |                       55 |              198236           | 0.11%              | 0.08%       |          220 |              165 | 75.0%            |
| account_10 |                       53 |              183916           | 0.12%              | 0.09%       |          212 |              159 | 75.0%  

| Underlying   |   Total Abs Val Quantity |   Total Abs Val Trans Net Amt | commission_trans   | csa_trans   |   Commission |   total_csa_cost | portion_to_csa   |
|:-------------|-------------------------:|------------------------------:|:-------------------|:------------|-------------:|-----------------:|:-----------------|
| SPX          |                    86253 |                   2.86738e+08 | 0.12%              | 0.09%       |       345012 |           258759 | 75.0%  
## By Buy/Sell
|                        |   Quantity |     Trans Net Amt | commission_trans   | csa_trans   |   Commission |   total_csa_cost | portion_to_csa   |
|:-----------------------|-----------:|------------------:|:-------------------|:------------|-------------:|-----------------:|:-----------------|
| ('account_10', 'Buy')  |         27 |   98261.1         | 0.11%              | 0.08%       |          108 |               81 | 75.0%            |
| ('account_10', 'Sell') |        -26 |  -85655.2         | 0.12%              | 0.09%       |          104 |               78 | 75.0%            |
| ('account_11', 'Buy')  |         73 |  261866           | 0.11%              | 0.08%       |          292 |              219 | 75.0%            |
| ('account_11', 'Sell') |        -68 | -222381           | 0.12%              | 0.09%       |          272 |              204 | 75.0%            |
| ('account_12', 'Buy')  |        268 |  905654           | 0.12%              | 0.09%       |         1072 |              804 | 75.0%            |
| ('account_12', 'Sell') |       -252 | -763630           | 0.13%              | 0.1%        |         1008 |              756 | 75.0%            |
| ('account_13', 'Buy')  |        129 |  868793           | 0.06%              | 0.04%       |          516 |              387 | 75.0%            |
| ('account_13', 'Sell') |       -117 | -695680           | 0.07%              | 0.05%       |          468 |              351 | 75.0%            |
| ('account_14', 'Buy')  |        117 |  651954           | 0.07%              | 0.05%       |          468 |              351 | 75.0%            |
| ('account_14', 'Sell') |       -106 | -534912           | 0.08%              | 0.06%       |          424 |              318 | 75.0%            |
| ('account_22', 'Buy')  |         53 |  186669           | 0.11%              | 0.09%       |          212 |              159 | 75.0%            |
| ('account_22', 'Sell') |        -49 | -153238           | 0.13%              | 0.1%        |          196 |              147 | 75.0%            |
| ('account_23', 'Buy')  |         52 |  184555           | 0.11%              | 0.08%       |          208 |              156 | 75.0%            |
| ('account_23', 'Sell') |        -49 | -153238           | 0.13%              | 0.1%        |          196 |              147 | 75.0%            |
| ('account_25', 'Buy')  |        192 |       1.2743e+06  | 0.06%              | 0.05%       |          768 |              576 | 75.0%            |
| ('account_25', 'Sell') |       -179 |      -1.00728e+06 | 0.07%              | 0.05%       |          716 |              537 | 75.0%            |
| ('account_26', 'Buy')  |      43003 |       1.4893e+08  | 0.12%              | 0.09%       |       172012 |           129009 | 75.0%            |
| ('account_26', 'Sell') |     -40479 |      -1.25729e+08 | 0.13%              | 0.1%        |       161916 |           121437 | 75.0%            |
| ('account_27', 'Buy')  |         39 |   31499.1         | 0.5%               | 0.37%       |          156 |              117 | 75.0%            |
| ('account_27', 'Sell') |        -36 |  -24783.2         | 0.58%              | 0.44%       |          144 |              108 | 75.0%            |
| ('account_28', 'Buy')  |        124 |  442291           | 0.11%              | 0.08%       |          496 |              372 | 75.0%            |
| ('account_28', 'Sell') |       -117 | -358262           | 0.13%              | 0.1%        |          468 |              351 | 75.0%            |
| ('account_29', 'Buy')  |         28 |  103035           | 0.11%              | 0.08%       |          112 |               84 | 75.0%            |
| ('account_29', 'Sell') |        -27 |  -95201.1         | 0.11%              | 0.09%       |          108 |               81 | 75.0%            |
| ('account_30', 'Buy')  |        118 |  476129           | 0.1%               | 0.07%       |          472 |              354 | 75.0%            |
| ('account_30', 'Sell') |       -109 | -403819           | 0.11%              | 0.08%       |          436 |              327 | 75.0%            |
| ('account_31', 'Buy')  |         58 |  236966           | 0.1%               | 0.07%       |          232 |              174 | 75.0%            |
| ('account_31', 'Sell') |        -54 | -200880           | 0.11%              | 0.08%       |          216 |              162 | 75.0%            |
| ('account_32', 'Buy')  |         53 |  212465           | 0.1%               | 0.07%       |          212 |              159 | 75.0%            |
| ('account_32', 'Sell') |        -49 | -179952           | 0.11%              | 0.08%       |          196 |              147 | 75.0%            |
| ('account_8', 'Buy')   |        106 |  700835           | 0.06%              | 0.05%       |          424 |              318 | 75.0%            |
| ('account_8', 'Sell')  |        -96 | -564327           | 0.07%              | 0.05%       |          384 |              288 | 75.0%            |

|                 |   Quantity |   Trans Net Amt | commission_trans   | csa_trans   |   Commission |   total_csa_cost | portion_to_csa   |
|:----------------|-----------:|----------------:|:-------------------|:------------|-------------:|-----------------:|:-----------------|
| ('SPX', 'Buy')  |      44440 |     1.55566e+08 | 0.11%              | 0.09%       |       177760 |           133320 | 75.0%            |
| ('SPX', 'Sell') |     -41813 |    -1.31173e+08 | 0.13%              | 0.1%        |       167252 |           125439 | 75.0% 
