

# This is the begging of my simulation
# we're going to strat with 1000 diploid individuals
from random import randrange
import matplotlib.pyplot as plt
# import plotly.plotly as py

# ipopulation makes the inital population. Here I made half of the population
# start with the genotypy [0, 0] and the other half [1, 1]
# can track by individual. I used a dictionary to index the data


def ipopulation(num):
    pop = {}
    for i in range(0, num):
        pop[i] = [0, 0]
        if i >= (num / 2):
            pop[i] = [1, 1]
    return pop
# gamwtes adds in the fitness level. Can add in the phenotype, but I found it
# is unnessaicary here it is labled as a, b, c.
# reproduction is how many potential gametes per gene


def gametes(pop, fitness00, fitness01_10, fitness11, repoduction):
    fitness = {}
    for i in pop:
        if pop[i] == [0, 0]:
            fitness[i] = [pop[i], fitness00, "a"]
        if pop[i] == [0, 1] or pop[i] == [1, 0]:
            fitness[i] = [pop[i], fitness01_10, "b"]
        if pop[i] == [1, 1]:
            fitness[i] = [pop[i], fitness11, "c"]
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

    return nextgen

# random is a function that picks out the correct amount of 0's and 1's

# change 2000 to number


def random(nextgerneration, num, mutation_rate):
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
                genechosen_change.append(1)
            if i == 1:
                genechosen_change.append(0)
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
    for i in newgeneration:
        if newgeneration[i] == [0, 0]:
            count0 = count0 + 2
        if newgeneration[i] == [0, 1] or newgeneration[i] == [1, 0]:
            count0 = count0 + 1
            count1 = count1 + 1
        if newgeneration[i] == [1, 1]:
            count1 = count1 + 2
    return count0, count1

# count counts the phenotype of the individuals
# A = (0,0), B = (0,1) or (1,0), C = (1,1)


def count(newgeneration):
    countA = 0
    countB = 0
    countC = 0
    for i in newgeneration:
        if newgeneration[i] == [0, 0]:
            countA = countA + 1
        if newgeneration[i] == [0, 1] or newgeneration[i] == [1, 0]:
            countB = countB + 1
        if newgeneration[i] == [1, 1]:
            countC = countC + 1
    return countA, countB, countC

# multiple_generations takes the inital population and runs it n geration times


def multiple_generations(initalpop, n, num):
    count_n = 1
# fitness1 for (0,0), fitness2 for (0,1) and (1,0), fitness3 for (1,1)
    fitness1 = 0.9
    fitness2 = 1.1
    fitness3 = 0.9
# reproduction is how many potential gametes per gene
    repoduction = 100.0
    mutation_rate = 20000
# while loop keeps track of generations and changs the population from the
# intinal population to the next geration after the first generation
    while count_n <= n:
        if count_n == 1:
            pop = initalpop
        nextgerneration = gametes(
            pop, fitness1, fitness2, fitness3, repoduction)
        genechosen, genechosen_change = random(
            nextgerneration, num, mutation_rate)
        newgeneration = (pairing(genechosen_change, num))
        count_n = count_n + 1
        if count_n > 1:
            pop = newgeneration
        # to check count the amount of 1's and 0's
        count0, count1 = icount(newgeneration)
        print(count0, count1)
    countA, countB, countC = count(newgeneration)
# countA is total number of (0,0) individuals
# countB is total number of (0,1) and (1,0) individuals
# countC is total number of (1,1) individuals
    return countA, countB, countC

# running the functions
# a = number of individuals with (0,0)
# b = number of individuals with (0,1) and (1,0)
# c = number of individuals with (1,1)


# comment below to stop running when i use a different file
# initalpop = ipopulation(1000)
# multiple_generations(ipop, number of generations, number of individuals)
# a, b, c = multiple_generations(initalpop, 1000, 1000)
# print (a, b, c)

# bargraph of countA, countB and countC.
# x = ('00', '01', '11')
# y = [a, b, c]
# N = len(y)
# width = 1 / 1.5
# plt.bar(x, y, width, color="blue")
# plt.xlabel('Phenotype')
# plt.ylabel('Total')
# plt.title('Simulation')
# plt.show()
print("hello")
