#data analyzer, organizes data from csv files
# add visual graph with matplotlib
# make program read other types of files
import matplotlib.pyplot as plt
import pandas as pd

data = input('Enter csv file name:')
datacsv = str(data)

num = pd.read_csv(datacsv)

print('Min:' , num.min())
print('Max:' , num.max())
print('Mean:', num.mean())
print('Median:', num.median())
print('Standard Deviation:', num.std())



