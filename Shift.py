# I am thinking about making a change in the the s at generation n
# maybe something similar to the fix2??
# somehow get s to change an if statement?
import matplotlib.pyplot as plt
from Individual_based_sim import gametes, random, icount, count, pairing


def ipopulationcontrol(popnum, per00, per10, per11):
    pop = {}
    allele_feq = (popnum * (per11 / 100) + popnum * (per10 / 200)) / popnum
    for i in range(0, popnum):
        pop[i] = [0, 0]
        if i >= (popnum * (per00 / 100)):
            pop[i] = [1, 0]
        if i >= (popnum * (per00 / 100) + popnum * (per10 / 100)):
            pop[i] = [1, 1]
    return pop, allele_feq


def Fixing(initalpop, num, mutation_rate, max_gen, fixation, sel_coe,
           sel_coe2, genX):
    count_n = 1
    # fitness1 for (0,0), fitness2 for (0,1) and (1,0), fitness3 for (1,1)
    fitness1 = 1.0 - (2 * sel_coe)
    fitness2 = 1.0 - sel_coe
    fitness3 = 1.0
    # reproduction is how many potential gametes per gene
    repoduction = 100.0
    pop = initalpop
    # while loop keeps track of generations and changs the population from the
    # intinal population to the next geration after the first generation
    plt.ion()  # Note this correction

    plt.axis([0, max_gen, 0, 1])

    x = list()
    y = list()

    while True:
        nextgerneration = gametes(
            pop, fitness1, fitness2, fitness3, repoduction)
        genechosen, genechosen_change = random(
            nextgerneration, num, mutation_rate)
        newgeneration = (pairing(genechosen_change, num))
        count_n = count_n + 1
        if count_n == genX:
            fitness1 = 1.0 - (2 * sel_coe2)
            fitness2 = 1.0 - sel_coe2
            fitness3 = 1.0
        pop = newgeneration
        # to check count the amount of 1's and 0's
        count0, count1 = icount(newgeneration)
        allele_feq = (count1 / (count0 + count1))
        # print(count1)
        print(allele_feq)

        x.append(count_n)
        y.append(allele_feq)
        plt.scatter(count_n, allele_feq)
        plt.show()
        plt.pause(0.0001)
        if allele_feq == 1:
            break
        if allele_feq == 0:
            break
    return count_n


# sel_coe is selection coefencent
population_size = 1000
sel_coe = .1
sel_coe2 = -.1
mutationrate = 100
GenX = 600


initalpop, allele_feq = ipopulationcontrol(population_size, 10, 50, 40)
print(count(initalpop))
print(allele_feq)
# Fixing(ipop, number of individuals, mutation, maxgen4graph, allele_feq,
# the selection coefficents, generation where the change happens)


year = Fixing(initalpop, population_size, mutationrate,  1000, allele_feq,
              sel_coe, sel_coe2, GenX)

print(year)
