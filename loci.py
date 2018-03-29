
# try 2 loci
# haplod so there will be 4 combos
# go by locus and by individual
from random import randrange
import matplotlib.pyplot as plt
import csv
import numpy as np
import matplotlib.patches as mpatches


def ipopulationcontrol(popnum, per00, per01, per10, per11):
    individuals = {}
    allele_feqloc1 = (popnum * (per11 / 100) + popnum * (per10 / 100)) / popnum
    allele_feqloc2 = (popnum * (per11 / 100) + popnum * (per01 / 100)) / popnum
    mean_phenotype = ((per00 / 100) * 4000 + (per01 / 100) * 5000 +
                      (per01 / 100) * 6000 + (per11 / 100) * 7000) / popnum
    for i in range(0, popnum):
        individuals[i] = [0, 0]
        if i >= (popnum * (per00 / 100)):
            individuals[i] = [0, 1]
        if i >= (popnum * (per00 / 100) + popnum * (per01 / 100)):
            individuals[i] = [1, 0]
        if i >= (popnum * (per00 / 100) + popnum * (per01 / 100) +
                 popnum * (per10 / 100)):
            individuals[i] = [1, 1]

    return individuals, allele_feqloc1, allele_feqloc2, mean_phenotype


def gametes(individuals, fitness00, fitness01, fitness10, fitness11,
            repoduction):
    fitness = {}
    for i in individuals:
        if individuals[i] == [0, 0]:
            fitness[i] = [individuals[i], fitness00]
        if individuals[i] == [0, 1]:
            fitness[i] = [individuals[i], fitness01]
        if individuals[i] == [1, 0]:
            fitness[i] = [individuals[i], fitness10]
        if individuals[i] == [1, 1]:
            fitness[i] = [individuals[i], fitness11]
    rep = {}
    for i in fitness:
        rep[i] = fitness[i][1] * repoduction
    nextgenloc1 = []
    nextgenloc2 = []
# nextgen is the list of 0's and 1's from the population. Adds the corrent
# amount of 0's and 1's
# j, k, v are counters for each while loop

    for i in rep:
        if individuals[i] == [0, 0]:
            j = 0
            while j < rep[i]:
                nextgenloc1.append(0)
                nextgenloc2.append(0)
                j = j + 1
        if individuals[i] == [1, 1]:
            k = 0
            while k < rep[i]:
                nextgenloc1.append(1)
                nextgenloc2.append(1)
                k = k + 1
        if individuals[i] == [0, 1]:
            v = 0
            while v < rep[i]:
                nextgenloc1.append(0)
                nextgenloc2.append(1)
                v = v + 1
        if individuals[i] == [1, 0]:
            w = 0
            while w < rep[i]:
                nextgenloc1.append(1)
                nextgenloc2.append(0)
                w = w + 1
    return nextgenloc1, nextgenloc2


def random(nextgernerationloc1, nextgernerationloc2, poppopnum, mutation_rate):
    genechosenloc1 = []
    genechosenloc2 = []
    for i in range(0, poppopnum * 2):
        random_index = randrange(0, len(nextgernerationloc1))
        genechosenloc1.append((nextgernerationloc1[random_index]))
        genechosenloc2.append((nextgernerationloc2[random_index]))
    genechosen_changeloc1 = []
    genechosen_changeloc2 = []
# genechosen_change is a list that will take the genes that were chosen and
# mutate them at a rate 1/20000
# global varrable
    for i in genechosenloc1:
        varable_index = randrange(1, mutation_rate + 1)
        if (varable_index % mutation_rate) == 0:
            if i == 0:
                genechosen_changeloc1.append(1)
            if i == 1:
                genechosen_changeloc1.append(0)
        else:
            genechosen_changeloc1.append(i)

    for i in genechosenloc2:
        varable_index = randrange(1, mutation_rate + 1)
        if (varable_index % mutation_rate) == 0:
            if i == 0:
                genechosen_changeloc2.append(1)
            if i == 1:
                genechosen_changeloc2.append(0)
        else:
            genechosen_changeloc2.append(i)
    return genechosen_changeloc1, genechosen_changeloc2


def pairing(genechosen_changeloc1, genechosen_changeloc2, popnum):
    newgen = {}
    k = 0
    i = 0
    while k < (popnum * 2):
        newgen[i] = [genechosen_changeloc1[k], genechosen_changeloc2[k]]
        i = i + 1
        k = i * 2
    return newgen

# icount was created to be able to count the amount of 0's and 1's in the
# population to see if the amount were changing (individual count)


def icount(newgeneration):
    countloc1_0 = 0
    countloc1_1 = 0
    countloc2_0 = 0
    countloc2_1 = 0
    for i in newgeneration:
        if newgeneration[i] == [0, 0]:
            countloc1_0 = countloc1_0 + 1
            countloc2_0 = countloc2_0 + 1
        if newgeneration[i] == [0, 1]:
            countloc1_0 = countloc1_0 + 1
            countloc2_1 = countloc2_1 + 1
        if newgeneration[i] == [1, 0]:
            countloc1_1 = countloc1_1 + 1
            countloc2_0 = countloc2_0 + 1
        if newgeneration[i] == [1, 1]:
            countloc1_1 = countloc1_1 + 1
            countloc2_1 = countloc2_1 + 1
    return countloc1_0, countloc1_1, countloc2_0, countloc2_1

# count counts the phenotype of the individuals
# A = (0,0), B = (0,1), C = (1,0), D = (1,1)


def count(newgeneration):
    countA = 0
    countB = 0
    countC = 0
    countD = 0
    for i in newgeneration:
        if newgeneration[i] == [0, 0]:
            countA = countA + 1
        if newgeneration[i] == [0, 1]:
            countB = countB + 1
        if newgeneration[i] == [1, 0]:
            countC = countC + 1
        if newgeneration[i] == [1, 1]:
            countD = countD + 1
    return countA, countB, countC, countD


# multiple_generations takes the inital population and runs it n geration times


def sim(initalpop, popnum, mutation_rate, sel_coe, allele_feqloc1,
        allele_feqloc2, repoduction, mean_phenotype, genend):
    count_n = 1
    # fitness1 for (0,0), fitness2 for (0,1), fitness3 for (0,1)
    # fitness4 for (1,1)
    fitness1 = 1.0
    fitness2 = 1.0 + sel_coe
    fitness3 = 1.0 + sel_coe
    fitness4 = 1.0
    loci1fit_0 = (allele_feqloc2) * (fitness2) + (
        (1 - allele_feqloc2) * (fitness1))
    loci1fit_1 = (allele_feqloc2) * (fitness4) + (
        (1 - allele_feqloc2) * (fitness3))
    loci2fit_0 = (1 - allele_feqloc1) * (fitness1) + (
        (allele_feqloc1) * (fitness3))
    loci2fit_1 = (1 - allele_feqloc1) * (fitness2) + (
        (allele_feqloc1) * (fitness4))
    pop = initalpop
    mean_phenotype = mean_phenotype
    myFile = open('twoloci2.csv', 'w')
    myFields = ['population', 'mu', 'allele_feq1', 'allele_feq2',
                'mean_phenotype', 'generation', 'pheno_of_00', 'fitness_00',
                'pheno_of_01', 'fitness_01', 'pheno_of_10', 'fitness_10',
                'pheno_of_11', 'fitness_11', 'phenotype_00', 'phenotype_01',
                'phenotype_10', 'phenotype_11', 'loci1fit_0', 'loci1fit_1',
                'loci2fit_0', 'loci2fit_1']
    writer = csv.DictWriter(myFile, fieldnames=myFields)
    writer.writeheader()
    writer.writerow(
        {'population': popnum, 'mu': (1 / mutation_rate),
         'allele_feq1': allele_feqloc1, 'allele_feq2': allele_feqloc2,
         'mean_phenotype': mean_phenotype, 'generation': count_n,
         'pheno_of_00': 4, 'fitness_00': fitness1,
         'pheno_of_01': 5, 'fitness_01': fitness2,
         'pheno_of_10': 6, 'fitness_10': fitness3,
         'pheno_of_11': 7, 'fitness_11': fitness4,
         'phenotype_00': per00 * popnum / 100,
         'phenotype_01': per01 * popnum / 100,
         'phenotype_10': per10 * popnum / 100,
         'phenotype_11': per11 * popnum / 100,
         'loci1fit_0': loci1fit_0, 'loci1fit_1': loci1fit_1,
         'loci2fit_0': loci2fit_0, 'loci2fit_1': loci2fit_1})

    # plt.ion()  # Note this correction
    # fig = plt.figure()
    # plt.axis([0, genend, 4, 7])
    # plt.title('Phenotype')
    # plt.xlabel('Time (generations)')
    # plt.ylabel('Phenotype')
    # blue = mpatches.Patch(color='blue')
    # plt.legend(handles=[blue])
    # x = list()
    # y = list()
    # plt.scatter(count_n, mean_phenotype, c='blue')
    # x.append(count_n)
    # y.append(mean_phenotype)
    while count_n < genend:

        # plt.scatter(count_n, mean_phenotype, c='blue')
        # x.append(count_n)
        # y.append(mean_phenotype)

        # plt.show()
        # plt.pause(0.0001)
        nextgenloc1, nextgenloc2 = gametes(
            pop, fitness1, fitness2, fitness3, fitness4,
            repoduction)
        genechosen_changeloc1, genechosen_changeloc2 = random(
            nextgenloc1, nextgenloc2, popnum, mutation_rate)
        newgeneration = (pairing(
            genechosen_changeloc1, genechosen_changeloc2, popnum))
        countloc1_0, countloc1_1, countloc2_0, countloc2_1 = icount(
            newgeneration)
        countA, countB, countC, countD = count(newgeneration)
        allele_feqloc1 = (countloc1_1 / (countloc1_0 + countloc1_1))
        allele_feqloc2 = (countloc2_1 / (countloc2_0 + countloc2_1))
        mean_phenotype = (countA * 4 + countB * 5 + countC * 6 +
                          countD * 7) / popnum
        count_n = count_n + 1
        pop = newgeneration
        print(count_n)
        loci1fit_0 = (allele_feqloc2) * (fitness2) + (
            (1 - allele_feqloc2) * (fitness1))
        loci1fit_1 = (allele_feqloc2) * (fitness4) + (
            (1 - allele_feqloc2) * (fitness3))
        loci2fit_0 = (1 - allele_feqloc1) * (fitness1) + (
            (allele_feqloc1) * (fitness3))
        loci2fit_1 = (1 - allele_feqloc1) * (fitness2) + (
            (allele_feqloc1) * (fitness4))
# heres where i will be making a csv
# for frequency distribution and mean phenotype
# allele_feq and mean_phenotype

        writer.writerow(
            {'population': popnum, 'mu': (1 / mutation_rate),
             'allele_feq1': allele_feqloc1, 'allele_feq2': allele_feqloc2,
             'mean_phenotype': mean_phenotype, 'generation': count_n,
             'pheno_of_00': 4, 'fitness_00': fitness1,
             'pheno_of_01': 5, 'fitness_01': fitness2,
             'pheno_of_10': 6, 'fitness_10': fitness3,
             'pheno_of_11': 7, 'fitness_11': fitness4,
             'phenotype_00': countA, 'phenotype_01': countB,
             'phenotype_10': countC, 'phenotype_11': countD,
             'loci1fit_0': loci1fit_0, 'loci1fit_1': loci1fit_1,
             'loci2fit_0': loci2fit_0, 'loci2fit_1': loci2fit_1})


popnum = 1000
per00 = 25
per01 = 25
per10 = 25
per11 = 25
mutation_rate = 10000
sel_coe = -0.2
repoduction = 50
genend = 5000

initalpop, allele_feqloc1, allele_feqloc2, mean_phenotype = ipopulationcontrol(
    popnum, per00, per01, per10, per11)
sim(initalpop, popnum, mutation_rate, sel_coe, allele_feqloc1,
    allele_feqloc2, repoduction, mean_phenotype, genend)
