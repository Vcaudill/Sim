from multiTT import fit_test_sim


path = "/Users/victoria/Desktop/Sim/"
folder = "Fitness_trials_100_.02/"
special = "fit_test"
poppopnum = 1000  # population size
loci = locus = 10  # number of loci
opfit = (loci / 2)  # the first opfit
repoduction = 50  # number used to increase replication output
mutation_rate = 1 / 10000
# how likely something will mutate 1/(whatever u put)
inver_mutation_rate = round(1 / mutation_rate)
rate = .2  # the percentage of 0 or 1 to be in population (1-rate, rate) (0, 1)
genend = 100  # what generation simulation will end at (this will change later on)
sigma = (.25 * loci)  # how wide the bell curve is
stop = .99  # this is where the fitnnes reaches this value the simulation will stop
trial_times = 100
trial = 0
# name = "/".join([path, 'popsize'str(poppopnum), str(loci)])
name = path + folder + special + '_popsize_' + str(poppopnum) + '_loci_' + str(
    loci) + '_opfit_' + str(opfit) + '_mu_' + str(
    (1 / inver_mutation_rate)) + '_sigma_' + str(
    sigma) + "_starting_rate_" + str(rate) + '_trial_' + str(trial) + ".csv"


for i in range(1, trial_times + 1):
    print("trial", i)
    name = path + folder + special + '_popsize_' + str(poppopnum) + '_loci_' + str(
        loci) + '_opfit_' + str(opfit) + '_mu_' + str(
        (1 / inver_mutation_rate)) + '_sigma_' + str(
        sigma) + "_starting_rate_" + str(rate) + '_trial_' + str(i) + ".csv"
    fit_test_sim(poppopnum, loci, opfit, repoduction, inver_mutation_rate, rate, stop, name, sigma)
