import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import matplotlib.patches as mpatches

with open('twoloci1.csv', newline='') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        print(row)

df = pd.read_csv("twoloci2.csv")
# df.plot()  # plots all columns against index
ax = df.plot(kind='scatter', x='generation', y='loci1fit_1', c='red',
             label='Locus 1 Allele 1 ')
df.plot(kind='scatter', x='generation', y='loci2fit_1', c='blue',
        label='Locus 2 Allele 1', ax=ax)
plt.title('Fitness Over Time')
plt.xlabel('Time (generations)')
plt.ylabel('Allele Fitness')
ar = df.plot(kind='scatter', x='generation', y='loci1fit_0', c='green',
             label='Locus 1 Allele 0 ')
df.plot(kind='scatter', x='generation', y='loci2fit_0', c='purple',
        label='Locus 2 Allele 0', ax=ar)
# scatter plot
# df.plot(kind='density')  # estimate density function

# df.plot(kind='hist')  # histogram

plt.title('Fitness Over Time')
plt.xlabel('Time (generations)')
plt.ylabel('Allele Fitness')

aq = df.plot(kind='scatter', x='generation', y='allele_feq1', c='lightcoral',
             label='Locus 1 Allele 1 ')
df.plot(kind='scatter', x='generation', y='allele_feq2', c='c',
        label='Locus 2 Allele 1', ax=aq)
plt.title('Frequency Over Time')
plt.xlabel('Time (generations)')
plt.ylabel('Allele Frequency')
# plt.figure()
# d = pd.read_csv('twoloci1.csv')
tr = df.hist(column='allele_feq1', color='orchid', label='Locus 1 Allele 1')
df.hist(column='allele_feq2', color='darkblue', label='Locus 2 Allele 1', ax=tr)
plt.title('Frequency Over Time')
plt.xlabel('Allele Frequency')
plt.ylabel('Probability')
orchid = mpatches.Patch(color='orchid', label='Locus 1 Allele 1')
darkblue = mpatches.Patch(color='darkblue', label='Locus 2 Allele 1')
plt.legend(handles=[orchid, darkblue])

df.plot(kind='scatter', x='mean_phenotype', y='loci1fit_1', c='lime',
             label='Locus 1 Allele 1 ')

plt.title('Fitness Over Time')
plt.xlabel('Phenotype')
plt.ylabel('Fitness')

# plt.xticks([1, 2, 3, 4, 5], ['0', '1/10', '1/100', '1/1000', '1/10000'])
plt.show()
