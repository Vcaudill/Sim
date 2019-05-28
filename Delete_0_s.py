import csv
import os
import pandas as pd

basic_PATH = '/Users/victoria/Desktop/Sim/'  # Use your path
folder = "Loc_10"
outfolder = "no_0_Loc_10"

stop = .99
trials = 100
column = 'mean_fit'
PATHtoFILES = "".join([basic_PATH, folder + "/"])
PATHtooutFILES = "".join([basic_PATH, outfolder + "/"])
poppopnum = [1000, 10000, 100000, 1000000]  # population size
mutation_rate = [(1 / 1000), (1 / 10000), (1 / 100000), (1 / 1000000)]

for num in poppopnum:
    for mu in mutation_rate:
        inver_mutation_rate = round(1 / mu)
        folders = 'popsize_' + str(num) + '/_mu_' + str((1 / inver_mutation_rate))
        PATH = "".join([PATHtoFILES, folders + "/"])
        outPATH = "".join([PATHtooutFILES, folders + "/"])

        # Fetch all files in path
        fileNames = os.listdir(PATH)

        # Filter file name list for files ending with .csv
        fileNames = [file for file in fileNames if '.csv' in file]
        if not os.path.isdir(outPATH):
            os.makedirs(outPATH)  # this creates a new folder puuuurrrrfict
        # Loop over all files
        for file in fileNames:

            infile = "".join([PATH, file])
            outfile = "".join([outPATH, file])
            with open(infile, 'r') as myFile:
                header = myFile.readline()

                csv_file_in = csv.reader(myFile, delimiter=",")

                with open(outfile, 'w') as out:

                    writer = csv.writer(out)
                    csv_file_out = csv.writer(out, delimiter=",")

                # writer = csv.DictWriter(f, fieldnames=csv_header.keys())
                # writer.writeheader()
                    regen = 0
                    for row in csv.reader(myFile):

                        if row[14] == "20":
                            regen += 1

                            new_row = row[0:14]
                            new_row += [row[14], regen]
                            writer.writerow(new_row)

            df = pd.read_csv(outfile, header=None)
            csv_header = 'locus_1,locus_2,locus_3,locus_4,locus_5,locus_6,locus_7,locus_8,locus_9,locus_10,generation,population_size,mean_pheno,mean_fit,burnin'
            df.rename(columns={0: 'locus_1', 1: 'locus_2', 2: 'locus_3', 3: 'locus_4', 4: 'locus_5', 5: 'locus_6', 6: 'locus_7', 7: 'locus_8', 8: 'locus_9',
                               9: 'locus_10', 10: 'generation', 11: 'population_size', 12: "mean_pheno", 13: "mean_fit", 14: 'burnin', 15: 'newgen'}, inplace=True)
            df.to_csv(outfile, index=False)

'''
df = pd.read_csv(outfile)
df.rename(columns={16: 'name'}, inplace=True)
df.to_csv(outfile, index=False)

            csv_input = pd.read_csv(outfile)
            csv_input['Berries'] = 1
            csv_input.to_csv(outfile, index=False)
    with open("in.csv", "rb") as in_file:
    header = in_file.readline()
    csv_file_in = csv.reader(in_file, delimiter=" ")
    with open("out.csv","wb") as out_file:
        out_file.write(header)
        csv_file_out = csv.writer(out_file, delimiter=" ")
        for row in csv_file_in:
            csv_file_out.writerow([row[0], 10] + row[1:])
            '''
# myFile = open('countries.csv', 'w')
