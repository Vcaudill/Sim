import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import matplotlib.patches as mpatches
path = "/Users/victoria/Desktop/Sim/"
folder = "CSV/"
special = "multi_opfit"
poppopnum = 1000  # population size
loci = locus = 10  # number of loci
opfit = (loci / 2)  # the first opfit
opfit2 = (loci / 3)  # the second opfit
opfit3 = (loci / 1.5)  # the third opfit
repoduction = 50  # number used to increase replication output
inver_mutation_rate = 100000  # how likely something will mutate 1/(whatever u put)
rate = .5  # the percentage of 0 or 1 to be in population (1-rate, rate) (0, 1)
genend = 10000  # what generation simulation will end at (this will change later on)
sigma = (.25 * loci)  # how wide the bell curve is

# name = "/".join([path, 'popsize'str(poppopnum), str(loci)])
name = path + folder + 'popsize_' + str(poppopnum) + '_loci_' + str(
    loci) + '_opfit_' + str(opfit) + '_mu_' + str(
    (1 / inver_mutation_rate)) + '_genend_' + str(genend) + '_sigma_' + str(
    sigma) + "_starting_rate_" + str(rate) + special + ".csv"

# file = '/Users/victoria/Desktop/Sim/CSV/weight.csv'
# file = "/Users/victoria/Desktop/Sim/CSV/popsize_100000_loci_10_opfit_5.0_mu_0.001_genend_1000_sigma_2.5_starting_rate_1multi_opfit.csv"
file = name
with open(file, newline='') as myFile:
    reader = csv.reader(myFile)

df = pd.read_csv(file)
X = np.linspace(1, 500, 5000)
# df.plot()  # plots all columns against index

aq = df.plot(kind='scatter', x='generation', y='locus_1', alpha=0.3,
             c='orchid', label='Locus 1 Allele 1',
             title=('Frequency Over Time'))
aq.set_xlabel('Time (generations)')
df.plot(kind='scatter', x='generation', y='locus_2', alpha=0.3,
        c='darkblue',
        label='Locus 2 Allele 1', ax=aq)
df.plot(kind='scatter', x='generation', y='locus_3', alpha=0.3,
        c='red',
        label='Locus 3 Allele 1', ax=aq)
df.plot(kind='scatter', x='generation', y='locus_4', alpha=0.3,
        c='green',
        label='Locus 4 Allele 1', ax=aq)
df.plot(kind='scatter', x='generation', y='locus_5', alpha=0.3,
        c='yellow',
        label='Locus 5 Allele 1', ax=aq)
df.plot(kind='scatter', x='generation', y='locus_6', alpha=0.3,
        c='orange',
        label='Locus 6 Allele 1', ax=aq)
df.plot(kind='scatter', x='generation', y='locus_7', alpha=0.3,
        c='pink',
        label='Locus 7 Allele 1', ax=aq)
df.plot(kind='scatter', x='generation', y='locus_8', alpha=0.3,
        c='blue',
        label='Locus 8 Allele 1', ax=aq)
df.plot(kind='scatter', x='generation', y='locus_9', alpha=0.3,
        c='purple',
        label='Locus 9 Allele 1', ax=aq)
df.plot(kind='scatter', x='generation', y='locus_10', alpha=0.3,
        c='lightgreen',
        label='Locus 10 Allele 1', ax=aq)
aq.set_xlim(1, 5000)
aq.set_xlabel('Time (generations)')
aq.set_ylabel('Allele Frequency')
plt.show()

at = df.plot(kind='scatter', x='generation', y='mean_fit', alpha=0.3,
             c='black', label='Mean Fitness',
             title=('Calculated Means'))

df.plot(kind='scatter', x='generation', y='mean_pheno', alpha=0.3,
        c='red',
        label='Mean Phenotype', ax=at)
at.set_xlim(1, 1000)
at.set_xlabel('Time (generations)')
at.set_ylabel('Mean Value')

plt.show()
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = the formula?
plt.plot(x, y, linewidth=2.0)

plt.plot([1, 2, 3, 4], [7, 6, 5, 4], linewidth=2.0)

plt.show()
