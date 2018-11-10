from multiTT import fit_test_burnin_sim
import os

path = "/Users/victoria/Desktop/Sim/"

folder = "Fitness_burnin_0-5_1Div100000_pop_1000"
mypath = path + folder
special = "/fit_test"
poppopnum = 1000  # population size
loci = locus = 10  # number of loci
opfit = (0)  # the first opfit
opfit2 = (loci / 2)  # the second opfit
repoduction = 50  # number used to increase replication output
mutation_rate = 1 / 100000
# how likely something will mutate 1/(whatever u put)
inver_mutation_rate = round(1 / mutation_rate)
rate = .5  # the percentage of 0 or 1 to be in population (1-rate, rate) (0, 1)
genend = 100  # what generation simulation will end at (this will change later on)
sigma = (.25 * loci)  # how wide the bell curve is
stop = .99  # this is where the fitnnes reaches this value the simulation will stop
trial_times = 100
trial = 0
burnin_gen_min = 20

if not os.path.isdir(mypath):
    os.makedirs(mypath)
# name = "/".join([path, 'popsize'str(poppopnum), str(loci)])
name = path + folder + special + '_popsize_' + str(poppopnum) + '_loci_' + str(
    loci) + '_opfit_' + str(opfit) + '_opfit2_' + str(opfit2) + '_mu_' + str(
    (1 / inver_mutation_rate)) + '_sigma_' + str(
    sigma) + "_starting_rate_" + str(rate) + '_trial_' + str(trial) + ".csv"


for i in range(1, trial_times + 1):
    print("trial", i)
    name = path + folder + special + '_popsize_' + str(poppopnum) + '_loci_' + str(
        loci) + '_opfit_' + str(opfit) + '_mu_' + str(
        (1 / inver_mutation_rate)) + '_sigma_' + str(
        sigma) + "_starting_rate_" + str(rate) + '_trial_' + str(i) + ".csv"
    fit_test_burnin_sim(poppopnum, loci, opfit, opfit2, repoduction,
                        inver_mutation_rate, rate, stop, name, sigma, burnin_gen_min)
