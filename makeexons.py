#Shawn Thomas - shawnt@uga.edu - 2018
import csv
import pandas as pd
import os
import shutil
import glob
from itertools import groupby

def maketup(file1):
	df = pd.read_csv(file1)
	df = df.sort_values('forward gene start')
	df['start_end'] = df[['forward gene start', 'forward gene end']].apply(tuple, axis=1)
	return df['start_end']

def merge_intervals(intervals):
    """
    A simple algorithm can be used:
    1. Sort the intervals in increasing order
    2. Push the first interval on the stack
    3. Iterate through intervals and for each one compare current interval
       with the top of the stack and:
       A. If current interval does not overlap, push on to stack
       B. If current interval does overlap, merge both intervals in to one
          and push on to stack
    4. At the end return stack
    """
    sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
    merged = []

    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            #added this condition branch
            if higher[0] - lower[1] == 1:
                merged[-1] = (lower[0], higher[1])  # replace by merged interval
            #end addition. Also changed if below to elif
            # test for intersection between lower and higher:
            # we know via sorting that lower[0] <= higher[0]
            elif higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)  # replace by merged interval
            else:
                merged.append(higher)
    return merged

#read in all csv files in directory
cwd = os.getcwd()
path = cwd
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]


for file in result:
	x = maketup(file)

	y = merge_intervals(x)

	df = pd.read_csv(file)
	a = df.iloc[0]['chromosome number']
	b = df.iloc[0]['gene number']


	df1 = pd.DataFrame(y, columns = ['start','stop'])
	df1['chromosome number'] = a
	df1['gene number'] = b
	df1['exon number'] = df1.index + 1
    #this gives the exons a number based on their position in the sequence.

	print df1
	df1.to_csv('exons' + file, encoding='utf-8', index=False)

source = '/Users/shawnthomas/Desktop/asptest/baitssplit/singchrom/cleaned'
dest1 = '/Users/shawnthomas/Desktop/asptest/baitssplit/singchrom/cleaned/exons'

os.mkdir(dest1)
os.chdir(source)

files = os.listdir(source)

for f in files:
    if (f.startswith("exons")):
        shutil.move(f, dest1)

