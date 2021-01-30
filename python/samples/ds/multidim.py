'''
python script to read csv using pandas dataframe
'''

import pandas as pd
import numpy as np

from csv_stddev_mean import stddmean_csvparse

def dim3merge( casenames, dfarr):

    if(len(dfarr)<1):
        raise ValueError("dfarr has less than 1 elements")

    mi = pd.MultiIndex.from_product( [casenames, list(dfarr[0].columns)], names=['cases','cards'] )
    val = []
    for df in dfarr:
        for z in df.values.flatten():
            val.append(z)
    dim3 = pd.DataFrame(val , index = mi)
    return dim3

if __name__ == "__main__":

    c1s, c1m = stddmean_csvparse('~/Downloads/SOC_real_time_1.csv', 'today1')
    c2s, c2m = stddmean_csvparse('~/Downloads/SOC_real_time_1.csv', 'today2')
    c3s, c3m = stddmean_csvparse('~/Downloads/SOC_real_time_1.csv', 'today3')

    res = dim3merge( ['ideal','non ideal','practical'], [c1s, c2s, c3s] )

    ## get ideal case
    print(res.xs('ideal', level='cases').unstack(level=0))
    print(res.xs('non ideal', level='cases').unstack(level=0))
    print(res.xs('724342174', level='cards').unstack(level=0))
