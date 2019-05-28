#!/usr/local/bin/python3
import matplotlib.pyplot as plt
# from mean_from_CSV_files import CSV_mean
from no_0_mean import CSV_mean
# from combine_CSV import CSV_Combine
from no_0_combine_CSV import CSV_Combine
import numpy as np
import csv
import pandas as pd
import matplotlib.patches as mpatches
import math
import os
import pandas as pd


# Set your path to the folder containing the .csv files

basic_PATH = '/Users/victoria/Desktop/Sim/'  # Use your path
folder = "no_0_Loc_10"

stop = .99
trials = 100
column = 'mean_fit'
PATHtoFILES = "".join([basic_PATH, folder + "/"])
poppopnum = [1000, 10000, 100000, 1000000]  # population size
mutation_rate = [(1 / 1000), (1 / 10000), (1 / 100000), (1 / 1000000)]

for num in poppopnum:
    for mu in mutation_rate:
        inver_mutation_rate = round(1 / mu)
        folders = 'popsize_' + str(num) + '/_mu_' + str((1 / inver_mutation_rate))
        PATH = "".join([PATHtoFILES, folders + "/"])
# below is where the files are placed into 1 csv then the mean is caculated
# make sure number of trials is correct
        mean_file = "".join([PATH, 'analize/mean_file' + ".csv"])
        # Fetch all files in path
        fileNames = os.listdir(PATH)
        csv_out = "".join([PATH, 'analize/consolidated' + ".csv"])
        # if os.path.isfile('consolidated.csv'):
        #     os.remove(csv_out)

        if not os.path.isdir(csv_out):
            CSV_Combine(PATH, column)
            CSV_mean(PATH, column, trials, stop)

        # Filter file name list for files ending with .csv
        fileNames = [file for file in fileNames if '.csv' in file]

        # Loop over all files
        for file in fileNames:
            print(file)

            # Read .csv file and append to list
            df = pd.read_csv(PATH + file, index_col=0)
            # Create line for every file

            plt.plot(df.loc[:, 'newgen'], df.loc[:, 'mean_fit'], alpha=0.3,
                     c='gray')

        df_mean = pd.read_csv(mean_file, index_col=0)
        print(df_mean)

        plt.plot(df_mean.loc[:, 'newgen'], df_mean.loc[:, 'mean_fit'], alpha=0.5,
                 c='blue', linewidth=2.0)
        plt.title('Population Fitness Over Time')
        plt.suptitle(file)
        plt.xlabel('Time (generations)')
        plt.ylabel('Fitness')
        # Generate the plot
        graph_file = "".join([PATH, '/graph' + ".pdf"])
        plt.savefig(graph_file)
        plt.show()
