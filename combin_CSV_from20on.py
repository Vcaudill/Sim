import os
import pandas as pd
import csv


def CSV_Combine(PATH, column):
    csv_header = 'locus_1,locus_2,locus_3,locus_4,locus_5,locus_6,locus_7,locus_8,locus_9,locus_10,generation,population_size,mean_pheno,mean_fit,burnin'
    csv_out = "/".join([PATH, 'analize/consolidated_20on' + ".csv"])
    mypath = PATH + 'analize'

    if not os.path.isdir(mypath):
        os.makedirs(mypath)
    fileNames = os.listdir(PATH)
    csv_list = []

    for file in fileNames:
        if file.endswith('.csv'):
            csv_list.append(file)

    csv_merge = open(csv_out, 'w')
    csv_merge.write(csv_header)
    csv_merge.write('\n')

    for file in csv_list:
        with open(PATH + file, 'r') as f:
            next(f, None)
            for line in f:
                if line.startswith(csv_header):
                    next(line)
                    continue
                csv_merge.write(line)

    with open(csv_out, newline='') as myFile:
        # writer = csv.DictWriter(f, fieldnames=csv_header.keys())
        # writer.writeheader()
        reader = csv.reader(myFile)
        for row in reader:
            if row[14] != 0:
                myFile.write(row)
    myFile = open('countries.csv', 'w')
    # writer.writerow(row)
    # data = pd.read_csv(csv_out)
    # data = data.sort_values(by=['generation', column])
    # data.to_csv(csv_out, sep=',')
    return()


'''
    data = pd.read_csv(csv_out)

    # Alternative:
    # most_sales = data['sold'].max()
    # data['fitness'].values[3:5].mean()
    data = data.sort_values(by=['generation', column])
    data.to_csv(csv_out, sep=',')
'''
PATH = "/Users/victoria/Desktop/Sim/Loc_11/popsize_1000/_mu_0.001/"
column = 'mean_fit'
CSV_Combine(PATH, column)
