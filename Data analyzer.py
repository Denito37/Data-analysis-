#data analyzer, organizes data from csv files, and creates a histograph png
import matplotlib.pyplot as plt
import pandas as pd

data = input('Enter csv file name:')
datafile = str(data)

num = pd.read_csv(datafile)

print('Min:' , num.min())
print('Max:' , num.max())
print('Mean:', num.mean())
print('Median:', num.median())
print('Standard Deviation:', num.std())

num.plot.hist()
plt.savefig('test.png')


