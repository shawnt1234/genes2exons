#Shawn Thomas - shawnt@uga.edu - 2018
import pandas as pd
import glob, os
 
cwd = os.getcwd()
os.chdir(cwd)
results = pd.DataFrame([])
 
for counter, file in enumerate(glob.glob("exons*")):
    namedf = pd.read_csv(file, skiprows=0)
    results = results.append(namedf)
 
results.to_csv('aspexons.csv')
#this concatenates all of the remaining exons into one file