import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

with open('ind_sim_diffu.csv', newline='') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        print(row)

df = pd.read_csv("ind_sim_diffu.csv")
# df.plot()  # plots all columns against index
df.plot(kind='scatter', x='pace', y='outcome')  # scatter plot
# df.plot(kind='density')  # estimate density function
# df.plot(kind='hist')  # histogram
plt.title('Different Mu Values')
plt.xlabel('Mutation Rate')
plt.ylabel('P(A)')
plt.xticks([1, 2, 3, 4, 5], ['0', '1/10', '1/100', '1/1000', '1/10000'])
plt.show()
