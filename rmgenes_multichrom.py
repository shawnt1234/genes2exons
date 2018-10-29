#Shawn Thomas - shawnt@uga.edu - 2018
import csv
import pandas as pd
import os
import shutil
import glob
from itertools import groupby


#This fuction returns the files that contain multiple loci in different chromosomes
def findMultChr(file1):
	df = pd.read_csv(file1)
	df = df.sort_values('chromosome number')
	chrom = df.iloc[0]['chromosome number']
	a = df['chromosome number'].astype(str).str.contains(chrom)
	#print a
	b = "MultLociChr_"
	c = []
	if "False" in str(a):
		c = b + file1
		return c


#read in all csv files in directory
cwd = os.getcwd()
path = cwd
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]
#print(result)


#if the file contains multiple chromosomes rename it to MultLociChr_filename.csv
for file in result:
	x = findMultChr(file)
	print x
	if str(file) in str(x):
	 	os.rename(file, 'MultLociChr_' + file)


source = '/Users/shawnthomas/Desktop/asptest/baitssplit'
dest1 = '/Users/shawnthomas/Desktop/asptest/baitssplit/multichrom'
dest2 = '/Users/shawnthomas/Desktop/asptest/baitssplit/singchrom'

os.mkdir(dest1)
os.chdir(source)
os.mkdir(dest2)
os.chdir(source)

files = os.listdir(source)

for f in files:
    if (f.startswith("MultLociChr")):
        shutil.move(f, dest1)
    elif (f.endswith(".csv")):
        shutil.move(f, dest2)
#NOTE: I manually moved 'MultLociChr_filename.csv' file to separate folder
#need to find a way to automatically move files
