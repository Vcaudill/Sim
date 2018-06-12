from random import randrange
import csv
import math


def ipopulationcontrol(popnum, loci, rate):
    # this function creates a population with the correct nuber of loci
    # individuals is a dictionary
    individuals = {}
    # locivalue is a list that will stratout the correct number of loci
    for i in range(0, popnum):
        locivalue = []
        for j in range(1, loci + 1):
            varable_index = randrange(0, rate + 1)
            locivalue.append(varable_index)
        individuals[i] = locivalue
    return individuals


def calcgaz(num, sigma, opfit):
    value = 0
    value = math.exp(-math.pow(
        -(num - opfit), 2) / (2 * (math.pow(sigma, 2))))
    return value


def fecunity(individuals, opfit, repoduction, loci, sigma):
    genotype = {}
    # trying to count 0's eventyally 1's in the list of 0/1's
    for i in individuals:
        count = 0
        for x in individuals[i]:
            if x == 1:
                count += 1  #
            genotype[i] = count
    rep = {}
    # baised off of how far away you are from the optuim fitness (opfit)
    # rep = replication
    # sigma = (.25 * loci / 2)
    for i in genotype:
        rep[i] = calcgaz(genotype[i], sigma, opfit) * repoduction
    # part of the pool, but how to make it varable?
    nextgenlistDict = {}
    # print(rep)
    for i in range(1, locus + 1):
        nextgenlistDict["locus_" + str(i)] = []
    # for each loci in this dictionary need to repeat 0/1s nested for loops?
    for t in individuals:
        count = 0
        for l in nextgenlistDict:
            allele = individuals[t][count]
            count = count + 1
            j = 0
            while j < rep[t]:
                if allele == 0:
                    nextgenlistDict[l].append(0)
                if allele == 1:
                    nextgenlistDict[l].append(1)
                if allele > 1:
                    nextgenlistDict[l].append(9)

                j = j + 1

    return nextgenlistDict


def random(nextgenlistDict, poppopnum, inver_mutation_rate, locus):
    values = []
    values = list(nextgenlistDict.values())
    nextgenlistDict = {}
    for i in range(1, locus + 1):
        nextgenlistDict["locus_" + str(i)] = []
    newindividuals = {}
    for i in range(0, poppopnum):
        newvalues = []
        for j in values:
            random_index = randrange(0, len(values[1]))
            # print(j) was an exilent test to determin that the loci same
            varable_index = randrange(1, inver_mutation_rate + 1)
            if (varable_index % inver_mutation_rate) == 0:
                if j[random_index] == 0:
                    newvalues.append(1)
                if j[random_index] == 1:
                    newvalues.append(0)
            else:
                newvalues.append(j[random_index])
        newindividuals[i] = newvalues
    return newindividuals


def allele_freq_count(newindividuals, locus, poppopnum):
    allele_feq = {}
    # trying to count 0's eventyally 1's in the list of 0/1's
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
        # tracking 0's
        allele_feq[i] = (1 - (allele_feq[i] / poppopnum)) * 100

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


def sim(poppopnum, loci, opfit, repoduction, inver_mutation_rate, rate, genend):
    count_n = 1
    # count_n is counting the generations so we know what geration we are on
    individuals = ipopulationcontrol(poppopnum, loci, rate)
    allele_feq = allele_freq_count(individuals, locus, poppopnum)
    ave_geno, avaerage_fit = averages(individuals, locus, poppopnum, opfit,
                                      sigma)
    # do not use . at beginning will save in system and not as a shareable file

    allele_feq['generation'] = count_n
    allele_feq['population_size'] = poppopnum
    allele_feq['mu'] = (1 / inver_mutation_rate)
    allele_feq['mean_pheno'] = ave_geno
    allele_feq['mean_fit'] = avaerage_fit

    with open('/Users/victoria/Desktop/Sim/CSV/multino1part2.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=allele_feq.keys())
        writer.writeheader()
        writer.writerow(allele_feq)
        while count_n < genend:
            print(count_n)
            nextgenlistDict = fecunity(individuals, opfit, repoduction, loci,
                                       sigma)
            newindividuals = random(nextgenlistDict, poppopnum,
                                    inver_mutation_rate, locus)
            allele_feq = allele_freq_count(newindividuals, locus, poppopnum)
            ave_geno, avaerage_fit = averages(newindividuals, locus, poppopnum,
                                              opfit, sigma)
            count_n = count_n + 1
            if count_n == 100:
                print(newindividuals)
            if count_n == 300:
                print(newindividuals)
            if count_n == 500:
                print(newindividuals)
            if count_n == 700:
                print(newindividuals)
            if count_n == 999:
                print(newindividuals)
            allele_feq['generation'] = count_n
            allele_feq['population_size'] = poppopnum
            allele_feq['mu'] = (1 / inver_mutation_rate)
            allele_feq['mean_pheno'] = ave_geno
            allele_feq['mean_fit'] = avaerage_fit
            individuals = newindividuals
            # heres where i will be making a csv
            writer.writerow(allele_feq)


poppopnum = 1000
loci = locus = 10
opfit = (loci / 2)
repoduction = 50
inver_mutation_rate = 1000
rate = 1
genend = 1000
sigma = (.25 * loci)


sim(poppopnum, loci, opfit, repoduction, inver_mutation_rate, rate, genend)
