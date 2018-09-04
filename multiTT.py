from random import randrange
import csv
import math
import random


def weighted_choice_king(weights):
    # weights = [.6, .4] = [0,1]
    total = 0
    winner = 0
    for i, w in enumerate(weights):
        # enumerate is an automatic counter
        total += w
        if random.random() * total < w:
            winner = i
    return winner


def ipopulationcontrol(popnum, loci, rate):
    # this function creates a population with the correct nuber of loci
    # individuals is a dictionary
    individuals = {}
    # locivalue is a list that will stratout the correct number of loci
    for i in range(0, popnum):
        locivalue = []
        for j in range(1, loci + 1):
            locivalue.append(weighted_choice_king([1 - rate, rate]))
        individuals[i] = locivalue
    return individuals


def calcgaz(num, sigma, opfit):
    value = 0
    value = math.exp(-math.pow(
        -(num - opfit), 2) / (2 * (math.pow(sigma, 2))))
    return value


def fecunity(individuals, opfit, repoduction, loci, sigma):
    genotype = {}
    total1 = 0
    # count 1's in the list of 0/1's
    for i in individuals:
        count = 0
        for x in individuals[i]:
            if x == 1:
                count += 1  #
                total1 += 1
            genotype[i] = count
    rep = {}
    # baised off of how far away you are from the optuim fitness (opfit)
    # rep = replication
    # sigma = (.25 * loci / 2)
    for i in genotype:
        rep[i] = calcgaz(genotype[i], sigma, opfit) * repoduction
    # part of the pool, but how to make it varable?
    # rep of a number could sum and lace it in a list 0, 1
    nextgenlist = {}
    # print(rep)
    for i in range(1, locus + 1):
        nextgenlist["locus_" + str(i)] = []
    # for each loci in this dictionary need to repeat 0/1s nested for loops?
    count = 0
    for l in nextgenlist:
        num0 = 0
        num1 = 0
        for t in individuals:
            # t is individual
            if individuals[t][count] == 0:
                num0 += rep[t]
            if individuals[t][count] == 1:
                num1 += rep[t]
        count += 1
        nextgenlist[l] = [num0, num1]
    return nextgenlist


def random5(nextgenlist, poppopnum, inver_mutation_rate, locus):
    newindividuals = {}
    for i in range(0, poppopnum):
        newvalues = []
        for j in nextgenlist:
            varable_index = randrange(1, inver_mutation_rate + 1)
            new_allele = (weighted_choice_king(nextgenlist[j]))
            if (varable_index % inver_mutation_rate) == 0:
                if new_allele == 0:
                    newvalues.append(1)
                if new_allele == 1:
                    newvalues.append(0)
            else:
                newvalues.append(new_allele)
        newindividuals[i] = newvalues

    return newindividuals


def allele_freq_count(newindividuals, locus, poppopnum):
    allele_feq = {}
    # allele frequency count
    for i in range(1, locus + 1):
        allele_feq["locus_" + str(i)] = []
    for i in allele_feq:
        allele_feq[i] = 0
    for j in newindividuals:
        locuscount = 0
        for i in allele_feq:
            allele = newindividuals[j][locuscount]
            allele_feq[i] = allele + allele_feq[i]
            locuscount += 1
    for i in allele_feq:
        # tracking 1's
        allele_feq[i] = (allele_feq[i] / poppopnum) * 100

    return allele_feq


# average genotype and averge fitness
def averages(newindividuals, locus, poppopnum, opfit, sigma):
    total_1_allele = 0
    ave_pheno = 0
    for i in newindividuals:
        for loc in newindividuals[i]:
            if loc == 1:
                total_1_allele += 1  # for each individual at each locus i
                # am adding 1 for the total alleles

    ave_pheno = total_1_allele / (locus * poppopnum)
    # print(ave_geno)  # amnount of 1 in pop

    avaerage_fit = 0
    phenotype = {}
    for i in newindividuals:
        num_1_alleles = 0
        for x in newindividuals[i]:
            if x == 1:
                num_1_alleles += 1  #
            phenotype[i] = num_1_alleles
    # fitness baised off of how far away you are from the optuim fitness(opfit)
    for i in phenotype:
        avaerage_fit += calcgaz(phenotype[i], sigma, opfit)
        # print(avaerage_fit)
    avaerage_fit = avaerage_fit / (poppopnum)

    return ave_pheno, avaerage_fit


# multiple_generations takes the inital population and runs it n geration times


def sim(poppopnum, loci, opfit, opfit2, opfit3, repoduction, inver_mutation_rate, rate, genend, name):
    count_n = 1
    # count_n is counting the generations so we know what geration we are on
    individuals = ipopulationcontrol(poppopnum, loci, rate)
    print(individuals)
    allele_feq = allele_freq_count(individuals, locus, poppopnum)
    ave_geno, avaerage_fit = averages(individuals, locus, poppopnum, opfit,
                                      sigma)
    # do not use . at beginning will save in system and not as a shareable file
    allele_feq['generation'] = count_n
    allele_feq['population_size'] = poppopnum
    allele_feq['mu'] = (1 / inver_mutation_rate)
    allele_feq['mean_pheno'] = ave_geno
    allele_feq['mean_fit'] = avaerage_fit

    with open(name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=allele_feq.keys())
        writer.writeheader()
        writer.writerow(allele_feq)
        while count_n <= genend:
            print("generation", count_n)
            nextgenlistDict = fecunity(individuals, opfit, repoduction, loci,
                                       sigma)
            newindividuals = random5(nextgenlistDict, poppopnum,
                                     inver_mutation_rate, locus)
            allele_feq = allele_freq_count(newindividuals, locus, poppopnum)
            ave_geno, avaerage_fit = averages(newindividuals, locus, poppopnum,
                                              opfit, sigma)
            count_n = count_n + 1
            if count_n == 300:
                opfit = opfit2
            if count_n == 700:
                opfit = opfit3

            allele_feq['generation'] = count_n
            allele_feq['population_size'] = poppopnum
            allele_feq['mu'] = (1 / inver_mutation_rate)
            allele_feq['mean_pheno'] = ave_geno
            allele_feq['mean_fit'] = avaerage_fit
            individuals = newindividuals
            # heres where i will be making a csv
            writer.writerow(allele_feq)


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


sim(poppopnum, loci, opfit, opfit2, opfit3, repoduction, inver_mutation_rate, rate, genend, name)
