# import csv
import matplotlib.pyplot as plt

from Individual_based_sim import ipopulation, gametes, random, icount, \
    pairing


def Fixing(initalpop, num, mutation_rate, max_gen):
    count_n = 1
    # fitness1 for (0,0), fitness2 for (0,1) and (1,0), fitness3 for (1,1)
    fitness1 = 1.
    fitness2 = 1.0
    fitness3 = 1.
    # reproduction is how many potential gametes per gene
    repoduction = 100.0
    pop = initalpop
    fixation = 0.5
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
        fixation = (count1 / (count0 + count1))
        print(count0)
        print(count1)

        x.append(count_n)
        y.append(fixation)
        plt.scatter(count_n, fixation)
        plt.show()
        plt.pause(0.0001)
        if fixation == 1:
            print(fixation)
            print("here 1")
            return count_n
            break
        if fixation == 0:
            print(fixation)
            print("here 0")
            return count_n
            break
    return count_n


initalpop = ipopulation(1000)

# multiple_generations(ipop, number of individuals)


year = Fixing(initalpop, 1000, 100, 1000)

print(year)
