import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import matplotlib.patches as mpatches
file = '/Users/victoria/Desktop/Sim/CSV/1.0_1.2_1.2_1.2_trial4.csv'
with open(file, newline='') as myFile:
    reader = csv.reader(myFile)

df = pd.read_csv(file)
X = np.linspace(1, 500, 5000)
# df.plot()  # plots all columns against index


fig, axes = plt.subplots(1, 2, gridspec_kw={'width_ratios': [3, 1]})

aq = df.plot(kind='scatter', x='generation', y='allele_feq1', alpha=0.3,
             c='orchid', label='Locus 1 Allele 1 ', ax=axes[0],
             title=('Frequency Over Time'))
aq.set_xlabel('Time (generations)')
df.plot(kind='scatter', x='generation', y='allele_feq2', alpha=0.3,
        c='darkblue',
        label='Locus 2 Allele 1', ax=aq)
aq.set_xlim(1, 5000)
aq.set_xlabel('Time (generations)')
aq.set_ylabel('Allele Frequency')


tr = df.hist(column='allele_feq1', alpha=0.7, color='orchid', bins=30,
             weights=np.ones_like(df[df.columns[0]]) * 100. / len(df),
             label='Locus 1 Allele 1', orientation='horizontal', ax=axes[1])

# plt.ylabel('Allele Freq')
plt.xlabel('Probability')
df.hist(column='allele_feq2', alpha=0.7, color='darkblue', bins=30,
        weights=np.ones_like(df[df.columns[0]]) * 100. / len(df),
        label='Locus 2 Allele 1', ax=tr, orientation='horizontal')
plt.title('Frequency Percentage')
orchid = mpatches.Patch(color='orchid', label='Locus 1 Allele 1')
darkblue = mpatches.Patch(color='darkblue', label='Locus 2 Allele 1')


plt.legend(handles=[orchid, darkblue]).draggable()
plt.suptitle('Frequency', fontsize=16)

plt.subplots_adjust(left=0.1, wspace=0.145, top=0.8)

sc = df.plot(kind='scatter', x='generation', y='phenotype_00', alpha=0.3,
             c='firebrick', label='00')
df.plot(kind='scatter', x='generation', y='phenotype_01', alpha=0.3,
        c='darkturquoise',
        label='01', ax=sc)
df.plot(kind='scatter', x='generation', y='phenotype_10', alpha=0.3, c='plum',
        label='10', ax=sc)
df.plot(kind='scatter', x='generation', y='phenotype_11', alpha=0.3,
        c='darkgreen',
        label='11', ax=sc)
firebrick = mpatches.Patch(color='firebrick', label='00')
darkturquoise = mpatches.Patch(color='darkturquoise', label='01')
plum = mpatches.Patch(color='plum', label='10')
darkgreen = mpatches.Patch(color='darkgreen', label='11')


plt.legend(handles=[firebrick, darkturquoise, plum, darkgreen]).draggable()
sc.set_xlim(1, 5000)
plt.title('Frequency of Phenotype Over Time')
plt.xlabel('Time (generations)')
plt.ylabel('Phenotype Frequency')
plt.show()
