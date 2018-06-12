import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from Individual_based_sim import gametes, random, icount, count, pairing

# for example 1000, 30%, 50%, 20%
# allele_feq will be caculated by the perctages of the population set in ipopco
# allele_feq of the [1,1] allele


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


def Fixing(initalpop, num, mutation_rate, max_gen, fixation, sel_coe):
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
    fig = plt.figure()
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
        pop = newgeneration
        # to check count the amount of 1's and 0's
        count0, count1 = icount(newgeneration)
        allele_feq = (count1 / (count0 + count1))
        # print(count1)
        print(allele_feq)

        x.append(count_n)
        y.append(allele_feq)
        plt.title('Allele Frequency Vs. Time')
        plt.xlabel('Time (generations)')
        plt.ylabel('Allele Frequency')
        plt.scatter(count_n, allele_feq, c="blue")
        plt.show()
        plt.pause(0.0001)
        if allele_feq == 1:
            break
        if allele_feq == 0:
            break
    return count_n


# sel_coe is selection coefencent
population_size = 1000
sel_coe = -.2
mutationrate = 100

initalpop, allele_feq = ipopulationcontrol(population_size, 25, 50, 25)
print(count(initalpop))
print(allele_feq)
# multiple_generations(ipop, number of individuals, mutation, maxgen)


year = Fixing(initalpop, population_size, mutationrate,  1000, allele_feq,
              sel_coe)

print(year)
