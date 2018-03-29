import matplotlib.pyplot as plt
from random import randrange
import numpy as np
import matplotlib.patches as mpatches


def ipopulationcontrol(popnum, per00, per01, per11, per02, per12, per22):
    pop = {}
    allele_feq1 = (popnum * (per11 / 100) + popnum * (per01 / 200) +
                   popnum * (per12 / 200)) / popnum
    allele_feq2 = (popnum * (per22 / 100) + popnum * (per02 / 200) +
                   popnum * (per12 / 200)) / popnum
    for i in range(0, popnum):
        pop[i] = [0, 0]
        if i >= (popnum * (per00 / 100)):
            pop[i] = [1, 0]
        if i >= (popnum * (per00 / 100) + popnum * (per01 / 100)):
            pop[i] = [1, 1]
        if i >= (popnum * (per00 / 100) + popnum * (per01 / 100) +
                 popnum * (per11 / 100)):
            pop[i] = [0, 2]
        if i >= (popnum * (per00 / 100) + popnum * (per01 / 100) +
                 popnum * (per11 / 100) + popnum * (per02 / 100)):
            pop[i] = [1, 2]
        if i >= (popnum * (per00 / 100) + popnum * (per01 / 100) +
                 popnum * (per11 / 100) + popnum * (per02 / 100) +
                 popnum * (per12 / 100)):
            pop[i] = [2, 2]
    return pop, allele_feq1, allele_feq2


def gametes(pop, fitness00, fitness01, fitness11, fitness02, fitness12,
            fitness22, repoduction):
    fitness = {}
    for i in pop:
        if pop[i] == [0, 0]:
            fitness[i] = [pop[i], fitness00]
        if pop[i] == [0, 1] or pop[i] == [1, 0]:
            fitness[i] = [pop[i], fitness01]
        if pop[i] == [1, 1]:
            fitness[i] = [pop[i], fitness11]
        if pop[i] == [0, 2]or pop[i] == [2, 0]:
            fitness[i] = [pop[i], fitness02]
        if pop[i] == [2, 1] or pop[i] == [1, 2]:
            fitness[i] = [pop[i], fitness12]
        if pop[i] == [2, 2]:
            fitness[i] = [pop[i], fitness22]
    rep = {}
# rep is the replication value that multiples the fitness by the reproduction
# value
    for i in fitness:
        rep[i] = fitness[i][1] * repoduction
    nextgen = []
# nextgen is the list of 0's and 1's from the population. Adds the corrent
# amount of 0's and 1's
# j, k, v are counters for each while loop

    for i in rep:
        if pop[i] == [0, 0]:
            j = 0
            while j < 2 * rep[i]:
                nextgen.append(0)
                j = j + 1
        if pop[i] == [1, 1]:
            k = 0
            while k < 2 * rep[i]:
                nextgen.append(1)
                k = k + 1
        if pop[i] == [1, 0] or pop[i] == [0, 1]:
            v = 0
            while v < rep[i]:
                nextgen.append(0)
                nextgen.append(1)
                v = v + 1
        if pop[i] == [2, 0] or pop[i] == [0, 2]:
            a = 0
            while a < rep[i]:
                nextgen.append(0)
                nextgen.append(2)
                a = a + 1
        if pop[i] == [2, 2]:
            b = 0
            while b < 2 * rep[i]:
                nextgen.append(2)
                b = b + 1
        if pop[i] == [1, 2] or pop[i] == [2, 1]:
            c = 0
            while c < rep[i]:
                nextgen.append(2)
                nextgen.append(1)
                c = c + 1

    return nextgen

# random is a function that picks out the correct amount of 0's and 1's

# change 2000 to number
# c_to_ chance of changing to that allele


def random(nextgerneration, num, mutation_rate, c0to1, c1to0, c2to0):
    genechosen = []
    for i in range(0, num * 2):
        random_index = randrange(0, len(nextgerneration))
        genechosen.append((nextgerneration[random_index]))

    genechosen_change = []
# genechosen_change is a list that will take the genes that were chosen and
# mutate them at a rate 1/20000
# global varrable
    for i in genechosen:
        varable_index = randrange(1, mutation_rate + 1)
        if (varable_index % mutation_rate) == 0:
            if i == 0:
                var_0 = randrange(1, c0to1 + 1)
                if (var_0 % c0to1) == 0:
                    genechosen_change.append(1)
                else:
                    genechosen_change.append(2)
            if i == 1:
                var_1 = randrange(1, c1to0 + 1)
                if (var_1 % c1to0) == 0:
                    genechosen_change.append(0)
                else:
                    genechosen_change.append(2)
            if i == 2:
                var_2 = randrange(1, c2to0 + 1)
                if (var_2 % c2to0) == 0:
                    genechosen_change.append(0)
                else:
                    genechosen_change.append(1)
        else:
            genechosen_change.append(i)

    return genechosen, genechosen_change

# mutation is a function I created to see if a mutation had occered not used in
# in final simulation


def mutation(genechosen, genechosen_change, num):
    for i in range(0, num * 2):
        if genechosen_change[i] != genechosen[i]:
            return ("Mutation")
        else:
            return ("None")
# pairing is a function that takes the first random 0 or 1 and pair it with the
# next random 0 or 1


def pairing(genechosen_change, num):
    nextdip = {}
    k = 0
    i = 0
    while k < (num * 2):
        nextdip[i] = [genechosen_change[k], genechosen_change[k + 1]]
        i = i + 1
        k = i * 2
    return nextdip

# icount was created to be able to count the amount of 0's and 1's in the
# population to see if the amount were changing (individual count)


def icount(newgeneration):
    count0 = 0
    count1 = 0
    count2 = 0
    for i in newgeneration:
        if newgeneration[i] == [0, 0]:
            count0 = count0 + 2
        if newgeneration[i] == [0, 1] or newgeneration[i] == [1, 0]:
            count0 = count0 + 1
            count1 = count1 + 1
        if newgeneration[i] == [1, 1]:
            count1 = count1 + 2
        if newgeneration[i] == [2, 2]:
            count2 = count2 + 2
        if newgeneration[i] == [0, 2] or newgeneration[i] == [2, 0]:
            count0 = count0 + 1
            count2 = count2 + 1
        if newgeneration[i] == [2, 1] or newgeneration[i] == [1, 2]:
            count2 = count2 + 1
            count1 = count1 + 1
    return count0, count1, count2

# count counts the phenotype of the individuals
# A = (0,0), B = (0,1) or (1,0), C = (1,1)


def count(newgeneration):
    countA = 0
    countB = 0
    countC = 0
    countD = 0
    countE = 0
    countF = 0
    for i in newgeneration:
        if newgeneration[i] == [0, 0]:
            countA = countA + 1
        if newgeneration[i] == [0, 1] or newgeneration[i] == [1, 0]:
            countB = countB + 1
        if newgeneration[i] == [1, 1]:
            countC = countC + 1
        if newgeneration[i] == [2, 0]or newgeneration[i] == [0, 2]:
            countD = countD + 1
        if newgeneration[i] == [2, 1] or newgeneration[i] == [1, 2]:
            countE = countE + 1
        if newgeneration[i] == [2, 2]:
            countF = countF + 1
    return countA, countB, countC, countD, countE, countF


def Fixing(initalpop, num, mutation_rate, max_gen, allele_feq1, sel_coe, Stop,
           stopvalue):
    count_n = 1
    c0to1 = 2
    c1to0 = 2
    c2to0 = 2
    # fitness1 for (0,0), fitness2 for (0,1) and (1,0), fitness3 for (1,1)
    # fitness4 for (2,0), fitness5 for (2,1) and (1,2), fitness6 for (2,2)
    fitness1 = 1.0 - (2 * sel_coe)
    fitness2 = 1.0 - sel_coe
    fitness3 = 1.0
    fitness4 = 1.0 - (2 * sel_coe)
    fitness5 = 1.0 - sel_coe
    fitness6 = 1.0
    # reproduction is how many potential gametes per gene
    repoduction = 100.0
    pop = initalpop
    if Stop == 'n':
        plt.ion()  # Note this correction
        fig = plt.figure()
        plt.axis([0, max_gen, 0, 1])
        plt.title('Three Alleles')
        plt.xlabel('Time (generations)')
        plt.ylabel('Allele Frequency')
        red = mpatches.Patch(color='red', label='Allele 1')
        blue = mpatches.Patch(color='blue', label='Allele 2')
        green = mpatches.Patch(color='green', label='Allele 0')
        plt.legend(handles=[green, red, blue])

        x = list()
        y = list()
    # while loop keeps track of generations and changs the population from the
    # intinal population to the next geration after the first generation

    while True:
        nextgerneration = gametes(
            pop, fitness1, fitness2, fitness3, fitness4, fitness5, fitness6,
            repoduction)
        genechosen, genechosen_change = random(
            nextgerneration, num, mutation_rate, c0to1, c1to0, c2to0)
        newgeneration = (pairing(genechosen_change, num))
        count_n = count_n + 1
        pop = newgeneration
        # to check count the amount of 1's and 0's
        count0, count1, count2 = icount(newgeneration)
        allele_feq1 = (count1 / (count0 + count1 + count2))
        allele_feq2 = (count2 / (count0 + count1 + count2))
        allele_feq0 = (count0 / (count0 + count1 + count2))
        # print(count1)
        print(count0, count1, count2)
        cA, cB, cC, cD, cE, cF = count(newgeneration)

        if Stop == 'y':
            if count_n == stopvalue:
                break
        if Stop == 'n':

            x.append(count_n)
            y.append(allele_feq1)
            plt.scatter(count_n, allele_feq1, c='red')
            y.append(allele_feq2)
            plt.scatter(count_n, allele_feq2, c='blue')
            y.append(allele_feq0)
            plt.scatter(count_n, allele_feq0, c='green')
            plt.show()
            plt.pause(0.0001)
            if allele_feq1 == 1 and allele_feq2 == 1:
                break
            if allele_feq1 == 0 and allele_feq2 == 0:
                break
            if allele_feq1 == 0 and allele_feq2 == 1:
                break
            if allele_feq1 == 1 and allele_feq2 == 0:
                break
            if count_n == generations:
                break
    return count_n, count0, count1, count2, cA, cB, cC, cD, cE, cF


population_size = 1000
sel_coe = .0001
mutationrate = 10000
generations = 1000
Stop = 'n'
stopvalue = 1000

population_size = 1000
initalpop, allele_feq1, allele_feq2 = ipopulationcontrol(
    population_size, 16, 16, 16, 17, 17, 18)
print(allele_feq1)
print(allele_feq2)
print(count(initalpop))

year, count0, count1, count2, a, b, c, d, e, f = Fixing(initalpop,
                                                        population_size,
                                                        mutationrate,
                                                        generations,
                                                        allele_feq1, sel_coe,
                                                        Stop, stopvalue)

plt.show(block=True)
print (a, b, c, d, e, f)

# bargraph of countA, countB and countC.
x = ('00', '01', '11', '20', '12', '22')
y = [a, b, c, d, e, f]
N = len(y)
width = 1 / 1.5
plt.bar(x, y, width, color="blue")
plt.xlabel('Phenotype')
plt.ylabel('Total')
plt.title('Simulation')
plt.show()
