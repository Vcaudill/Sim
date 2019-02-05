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
folder = "Sigma_TEST_Fitness_burnin/"
loci = locus = 10
sigma = [(.1 * loci), (.2 * loci), (.25 * loci), (.5 * loci)]
stop = .99
trials = 100
column = 'mean_fit'

PATH = "".join([basic_PATH, folder + "/"])
for j in sigma:
    PATH2sig = "".join([PATH + "sigma" + str(j) + "/"])
    mean_file = "".join([PATH2sig, 'analize/mean_file' + ".csv"])
# Fetch all files in path
    fileNames = os.listdir(PATH2sig)
    csv_out = "".join([PATH2sig, 'analize/consolidated' + ".csv"])
# if os.path.isfile('consolidated.csv'):
#     os.remove(csv_out)

    if not os.path.isdir(csv_out):
        CSV_Combine(PATH2sig, column)
        CSV_mean(PATH2sig, column, trials, stop)

# Filter file name list for files ending with .csv
    fileNames = [file for file in fileNames if '.csv' in file]

    # Loop over all files
    for file in fileNames:
        print(file)

        # Read .csv file and append to list
        df = pd.read_csv(PATH2sig + file, index_col=0)
        # Create line for every file

        # plt.plot(df.loc[:, 'generation'], df.loc[:, 'mean_fit'], alpha=0.3,
        #         c='gray')

    df_mean = pd.read_csv(mean_file, index_col=0)
    print(df_mean)
    if (j == .1 * loci):
        Scolor = "orange"
        SigmaName = "Sigma = .1 * loci"
    if (j == .2 * loci):
        Scolor = "purple"
        SigmaName = "Sigma = .2 * loci"
    if (j == .25 * loci):
        Scolor = "blue"
        SigmaName = "Sigma = .25 * loci"
    if (j == .5 * loci):
        Scolor = "red"
        SigmaName = "Sigma = .5 * loci"
    plt.plot(df_mean.loc[:, 'generation'], df_mean.loc[:, 'mean_fit'], alpha=0.5,
             c=Scolor, linewidth=2.0)
    plt.title('Population Fitness Over Time')
    plt.suptitle(SigmaName)
    plt.xlabel('Time (generations)')
    plt.ylabel('Fitness')
    # Generate the plot
    graph_file = "".join([PATH2sig, '/graph' + ".pdf"])
    # plt.savefig(graph_file)
    plt.show()

'''
All of the sigma together
    graph_file = "".join([PATH, '/graphPFT' + ".pdf"])
    # plt.savefig(graph_file)
blue = mpatches.Patch(color='blue', label='.25 * loci')
red = mpatches.Patch(color='red', label='.5 * loci')
orange = mpatches.Patch(color='orange', label='.1 * loci')
purple = mpatches.Patch(color='purple', label='.2 * loci')
plt.legend(handles=[orange, purple, blue, red]).draggable()
plt.savefig(graph_file)
plt.show()
'''
