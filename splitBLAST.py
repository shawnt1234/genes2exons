#Shawn Thomas - shawnt@uga.edu - 2018
import csv
import pandas as pd
import os
from itertools import groupby

#import modified BLAST output and sort values based on bait code
df = pd.read_csv('asptarget.csv')
df = df.sort_values('gene number')

chrom = (df.at[1, 'chromosome number'])

print chrom
os.mkdir('baitssplit')
os.chdir('baitssplit')

#makes separate csv files for each gene number
for i, g in df.groupby('gene number'):
	g.to_csv('{}.csv'.format(i), header=True, index_label=False)
