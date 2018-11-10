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
# folder = "Fitness_burnin_0-5_1Div100000_pop_1000"
folder = "Fitness_burnin_0-5_1Div1000000_pop_1000"
# folder = "Fitness_burnin_0-5_1Div10000000_pop_1000"
# folder = "Fitness_burnin_0-5_1Div1000_pop_10000"
stop = .99
trials = 100
column = 'mean_fit'
PATH = "".join([basic_PATH, folder + "/"])
mean_file = "".join([PATH, 'analize/mean_file' + ".csv"])
# Fetch all files in path
fileNames = os.listdir(PATH)
csv_out = "".join([PATH, 'analize/consolidated' + ".csv"])
# if os.path.isfile('consolidated.csv'):
#     os.remove(csv_out)
'''
if not os.path.isdir(csv_out):
    CSV_Combine(PATH, column)
    CSV_mean(PATH, column, trials, stop)
'''
# Filter file name list for files ending with .csv
fileNames = [file for file in fileNames if '.csv' in file]

# Loop over all files
for file in fileNames:
    print(file)

    # Read .csv file and append to list
    df = pd.read_csv(PATH + file, index_col=0)
    # Create line for every file

    plt.plot(df.loc[:, 'generation'], df.loc[:, 'mean_fit'], alpha=0.3,
             c='gray')

df_mean = pd.read_csv(mean_file, index_col=0)
print(df_mean)

plt.plot(df_mean.loc[:, 'generation'], df_mean.loc[:, 'mean_fit'], alpha=0.5,
         c='blue', linewidth=2.0)
plt.title('Population Fitness Over Time')
plt.suptitle(file)
plt.xlabel('Time (generations)')
plt.ylabel('Fitness')
# Generate the plot
graph_file = "".join([PATH, '/graph' + ".pdf"])
plt.savefig(graph_file)
plt.show()
