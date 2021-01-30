'''
python script to read csv using pandas dataframe
'''

import pandas as pd

def stddmean_csvparse(filename, datestring):
    read = pd.read_csv(filename, delimiter=',')
    colhead = list(read.columns)
    colhead.pop(0) # delete first column

    rstdd = {}
    rmean = {}
    for c in colhead:
        row = read.loc[:, c]
        rstdd[c] = row.std()
        rmean[c] = row.mean()

    dfstdd = pd.DataFrame( [tuple(rstdd.values())], columns = colhead, index=[datestring])
    dfmean = pd.DataFrame( [tuple(rmean.values())], columns = colhead, index=[datestring])
    return dfstdd, dfmean

if __name__ == "__main__":

    dfstdd, dfmean = stddmean_csvparse('~/Downloads/SOC_real_time_1.csv', 'today')
    print(dfstdd)
    print(dfmean)
