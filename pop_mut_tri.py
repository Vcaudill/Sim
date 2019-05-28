from multiTT import fit_test_burnin_sim
import os

path = "/Users/victoria/Desktop/Sim/"
folder = "Pleuni_Test"

special = "/loci_100/"
path = path + folder + special
poppopnum = [1000, 10000, 100000, 1000000]  # population size
# poppopnum = [1000, 10000, 100000, 1000000]  # population size
loci = locus = 100  # number of loci
opfit = (0)  # the first opfit
opfit2 = (loci / 2)  # the second opfit
repoduction = 50  # number used to increase replication output
mutation_rate = [(1 / 10000), (1 / 100000), (1 / 1000000)]
# mutation_rate = [(1 / 1000), (1 / 10000), (1 / 100000), (1 / 1000000)]

# how likely something will mutate 1/(whatever u put)

rate = .5  # the percentage of 0 or 1 to be in population (1-rate, rate) (0, 1)
sigma = (.25 * loci)  # how wide the bell curve is
stop = .99  # the fitness reaches this value the simulation will stop
trial_times = 1
trial = 0
burnin_gen_min = 20

for num in poppopnum:
    for mu in mutation_rate:
        inver_mutation_rate = round(1 / mu)
        folder = 'popsize_' + str(num) + '/_mu_' + str((1 / inver_mutation_rate))
        mypath = path + folder
        if not os.path.isdir(mypath):
            os.makedirs(mypath)
# name = "/".join([path, 'popsize'str(poppopnum), str(loci)])
        for trial in range(1, trial_times + 1):
            print(folder, "trial", trial)
            name = mypath + '/_popsize_' + str(num) + '_loci_' + str(
                loci) + '_opfit_' + str(opfit) + '_opfit2_' + str(opfit2) + '_mu_' + str(
                (1 / inver_mutation_rate)) + '_sigma_' + str(
                sigma) + "_starting_rate_" + str(rate) + '_trial_' + str(trial) + ".csv"
            fit_test_burnin_sim(num, loci, opfit, opfit2, repoduction,
                                inver_mutation_rate, rate, stop, name, sigma, burnin_gen_min)
