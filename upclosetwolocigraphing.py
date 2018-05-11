import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import matplotlib.patches as mpatches
file = '/Users/victoria/Desktop/Sim/CSV/1.0_1.2_1.2_1.2_trial6.csv'
with open(file, newline='') as myFile:
    reader = csv.reader(myFile)

df = pd.read_csv(file)
X = np.linspace(1, 500, 5000)
# df.plot()  # plots all columns against index
ax = df.plot(kind='scatter', x='generation', y='loci1fit_1', c='red',
             label='Locus 1 Allele 1 ', alpha=0.3)
df.plot(kind='scatter', x='generation', y='loci2fit_1', c='blue',
        label='Locus 2 Allele 1', ax=ax, alpha=0.3)
ax.set_xlim(1, 500)
plt.title('Marginal Fitness')
plt.xlabel('Time (generations)')
plt.ylabel('Allele Fitness')
df.plot(kind='scatter', x='generation', y='loci1fit_0', alpha=0.3,
             c='green', label='Locus 1 Allele 0', ax=ax)
df.plot(kind='scatter', x='generation', y='loci2fit_0', alpha=0.3, c='purple',
        label='Locus 2 Allele 0', ax=ax)
ax.set_xlim(0, 500)
# scatter plot
# df.plot(kind='density')  # estimate density function

# df.plot(kind='hist')  # histogram

plt.title('Marginal Fitness')
plt.xlabel('Time (generations)')
plt.ylabel('Allele Fitness')

aq = df.plot(kind='scatter', x='generation', y='allele_feq1', alpha=0.3,
             c='lightcoral', label='Locus 1 Allele 1 ')
df.plot(kind='scatter', x='generation', y='allele_feq2', alpha=0.3, c='c',
        label='Locus 2 Allele 1', ax=aq)
aq.set_xlim(1, 500)
plt.title('Frequency Over Time')
plt.xlabel('Time (generations)')
plt.ylabel('Allele Frequency')
# plt.figure()
# d = pd.read_csv('twoloci1.csv')
tr = df.hist(column='allele_feq1', alpha=0.7, color='orchid', bins=20,
             weights=np.ones_like(df[df.columns[0]]) * 100. / len(df),
             label='Locus 1 Allele 1')
df.hist(column='allele_feq2', alpha=0.7, color='darkblue', bins=20,
        weights=np.ones_like(df[df.columns[0]]) * 100. / len(df),
        label='Locus 2 Allele 1', ax=tr)
plt.title('Frequency Count')
plt.xlabel('Allele Frequency')
plt.ylabel('Probability')
orchid = mpatches.Patch(color='orchid', label='Locus 1 Allele 1')
darkblue = mpatches.Patch(color='darkblue', label='Locus 2 Allele 1')
plt.legend(handles=[orchid, darkblue])

pf = df.plot(kind='scatter', x='pheno_of_00', y='fitness_00',
             alpha=0.3, c='k')
df.plot(kind='scatter', x='pheno_of_01', y='fitness_01',
             alpha=0.3, c='k', ax=pf)
df.plot(kind='scatter', x='pheno_of_10', y='fitness_10',
             alpha=0.3, c='k', ax=pf)
df.plot(kind='scatter', x='pheno_of_11', y='fitness_11',
             alpha=0.3, c='k', ax=pf)

plt.title('Fitness for Phenotype')
plt.xlabel('Phenotype')
plt.ylabel('Fitness')
# iloc[row slicing, column slicing]
dfname = df.rename(columns={'pheno_of_00': 'pheno', 'pheno_of_01': 'pheno',
                            'pheno_of_10': 'pheno', 'pheno_of_11': 'pheno'})
dfname = dfname.rename(columns={'fitness_00': 'fit', 'fitness_01': 'fit',
                                'fitness_10': 'fit', 'fitness_11': 'fit'})
df1 = dfname.iloc[[0, 2], 6:8]
df2 = dfname.iloc[[0, 2], 8:10]
df3 = dfname.iloc[[0, 2], 10:12]
df4 = dfname.iloc[[0, 2], 12:14]

frames = [df1, df2, df3, df4]
result = pd.concat(frames)

resultagain = pd.DataFrame(result)
print(resultagain)
x = resultagain['pheno']
y = resultagain['fit']
plt.plot(x, y, c='rebeccapurple')
plt.title('Fitness for Phenotype')
plt.xlabel('Phenotype')
plt.ylabel('Fitness')
# plt.xticks([1, 2, 3, 4, 5], ['0', '1/10', '1/100', '1/1000', '1/10000'])
plt.show()
