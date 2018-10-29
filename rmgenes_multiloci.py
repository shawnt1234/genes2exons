#Shawn Thomas - shawnt@uga.edu - 2018
import csv
import pandas as pd
import os
import shutil
import glob
from itertools import groupby

#This function sorts the by forward gene start then find difference between first and last forward gene start
#returns the files that have multiple loci (multiple loci is determined by >250kb difference)
def findMultLoci(file1):
	df = pd.read_csv(file1)
	df = df.sort_values('forward gene start')
	a = df['forward gene start'].iloc[-1] - df['forward gene start'].iloc[0]
	if abs(a) > 250000:
		b = "MultLociSame_"
		c = []
		c = b + file1
		return c


#read in all csv files in directory
cwd = os.getcwd()
path = cwd
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]


#if the file contains multiple loci rename it to MultLociSame_filename.csv
for file in result:
	x = findMultLoci(file)
	print x
	if str(file) in str(x):
	 	os.rename(file, 'MultLociSame_' + file)

source = '/Users/shawnthomas/Desktop/asptest/baitssplit/singchrom'
dest1 = '/Users/shawnthomas/Desktop/asptest/baitssplit/singchrom/multlocisame'
dest2 = '/Users/shawnthomas/Desktop/asptest/baitssplit/singchrom/cleaned'

os.mkdir(dest1)
os.chdir(source)
os.mkdir(dest2)
os.chdir(source)

files = os.listdir(source)

for f in files:
    if (f.startswith("MultLociSame")):
        shutil.move(f, dest1)
    elif (f.endswith(".csv")):
        shutil.move(f, dest2)

#NOTE: I manually moved 'MultLociSame_filename.csv' files to separate folder
#need to find a way to automatically move files
