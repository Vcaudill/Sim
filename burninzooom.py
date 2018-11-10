import matplotlib.pyplot as plt
from mean_from_CSV_files import CSV_mean
from combine_CSV import CSV_Combine
import numpy as np
import csv
import pandas as pd
import matplotlib.patches as mpatches
import math
import os
import pandas as pd


# Set your path to the folder containing the .csv files

basic_PATH = '/Users/victoria/Desktop/Sim/'  # Use your path
# folder = "Fitness_trials_100_.02"
# folder = "Fitness_trials_1000"
# folder = "fitnes_trials"
# folder = "Fitness_burnin_0-5_1Div10000"
folder = "Fitness_burnin_0-5_1Div10000000_pop_1000"
# folder = "Fitness_burnin_0-5_1Div1000_pop_10000"
# folder = "Fitness_burnin_0-5_1Div1000000_pop_1000"
stop = .99
trials = 100
split = 70
if folder == "Fitness_burnin_0-5_1Div10000000_pop_1000":
    end = 55000
column = 'mean_fit'
PATH = "".join([basic_PATH, folder + "/"])
mean_file = "".join([PATH, 'analize/mean_file' + ".csv"])
# Fetch all files in path
fileNames = os.listdir(PATH)
csv_out = "".join([PATH, 'analize/consolidated' + ".csv"])
# if os.path.isfile('consolidated.csv'):
#     os.remove(csv_out)
# if not os.path.isdir(csv_out):
# CSV_Combine(PATH, column)
# CSV_mean(PATH, column, trials, stop)

# Filter file name list for files ending with .csv
fileNames = [file for file in fileNames if '.csv' in file]
X = np.linspace(1, 500, 5000)
# df.plot()  # plots all columns against index
df_mean = pd.read_csv(mean_file, index_col=0)
end = max(df_mean['generation']) + 50
fig, axes = plt.subplots(1, 2, gridspec_kw={'width_ratios': [1, 5]})
# Loop over all files
for file in fileNames:
    print(file)

    # Read .csv file and append to list
    df = pd.read_csv(PATH + file, index_col=0)
    # Create line for every file
    aq = df.plot(x='generation', y='mean_fit', alpha=0.3, c='gray',
                 ax=axes[0], legend=None)

df_mean.plot(x='generation', y='mean_fit', alpha=0.5,
             c='blue', ax=aq, legend=None, linewidth=2.0)
aq.set_ylabel('Fitness')
aq.set_xlabel('')
aq.spines['right'].set_visible(False)
aq.set_xlim(1, split)
for file in fileNames:
    print(file)

    # Read .csv file and append to list
    df = pd.read_csv(PATH + file, index_col=0)
    # Create line for every file
    tr = df.plot(x='generation', y='mean_fit', alpha=0.5, c='gray',
                 ax=axes[1], legend=None)
# print(df_mean)
df_mean.plot(x='generation', y='mean_fit', alpha=0.5,
             c='blue', ax=tr, legend=None, linewidth=2.0)
tr.set_yticklabels([])
# tr.set_frame_on(False)
tr.spines['left'].set_visible(False)
tr.axes.get_yaxis().set_visible(False)
tr.set_xlabel('')
tr.set_xlim(split, end)
'''
plt.title('Population Fitness Over Time')
plt.suptitle(file)
plt.xlabel('Time (generations)')
plt.ylabel('Fitness')
'''
# Generate the plot
graph_file = "".join([PATH, '/graph2.1' + ".pdf"])
plt.subplots_adjust(left=0.1, wspace=0, top=.9)
# plt.legend().draggable()
# plt.title('Population Fitness Over Time', loc="left")
fig.suptitle('Population Fitness Over Time')
# fig.aspxlabel('Time (generations)')
fig.text(0.5, 0.04, 'Time (generations)', ha='center')
plt.ylabel('Fitness')
plt.savefig(graph_file)
plt.show()

# X = np.linspace(1, 500, 5000)
# df.plot()  # plots all columns against index

'''
aq = df.plot(kind='scatter', x='generation', y='allele_feq1', alpha=0.3,
             c='orchid', label='Locus 1 Allele 1 ', ax=axes[0],
             title=('Frequency Over Time'))
aq.set_xlabel('Time (generations)')
df.plot(kind='scatter', x='generation', y='allele_feq2', alpha=0.3,
        c='darkblue',
        label='Locus 2 Allele 1', ax=aq)
aq.set_xlim(1, 500)
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
'''
