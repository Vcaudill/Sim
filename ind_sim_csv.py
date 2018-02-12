# csv file form my Simulation
import csv
from Individual_based_sim import ipopulation, gametes, random, icount, \
    pairing


def multiple_generations_diffent_mew(initalpop, n, num, mutation_rate):
    count_n = 1
# fitness1 for (0,0), fitness2 for (0,1) and (1,0), fitness3 for (1,1)
    fitness1 = 0.9
    fitness2 = 0.9
    fitness3 = 0.9
# reproduction is how many potential gametes per gene
    repoduction = 100.0
    pop = initalpop

# while loop keeps track of generations and changs the population from the
# intinal population to the next geration after the first generation

    while count_n <= n:
        nextgerneration = gametes(
            pop, fitness1, fitness2, fitness3, repoduction)
        genechosen, genechosen_change = random(
            nextgerneration, num, mutation_rate)
        newgeneration = (pairing(genechosen_change, num))
        count_n = count_n + 1
        pop = newgeneration
        # to check count the amount of 1's and 0's
        count0, count1 = icount(newgeneration)

    return count0, count1


initalpop = ipopulation(1000)
# multiple_generations(ipop, number of generations, number of individuals)


def makCSV(initalpop, n, num, mr1, mr2, mr3, mr4, mr5):

    myFile = open('ind_sim_diffu.csv', 'w')
    n = 0
# run once 5 times but in one for loop instead of 5 had codeing mutation rate
# put into functon
    with myFile:
        myFields = ['population', 'mew', 'outcome', 'pace']
        writer = csv.DictWriter(myFile, fieldnames=myFields)
        writer.writeheader()
        for i in range(0, 5):
            a, b = multiple_generations_diffent_mew(
                initalpop, n, num, mr1)
            writer.writerow(
                {'population': num, 'mew': mr1, 'outcome': b /
                 (a + b), 'pace': 1})
        for i in range(0, 5):
            a, b = multiple_generations_diffent_mew(
                initalpop, n, num, mr2)
            writer.writerow(
                {'population': num, 'mew': mr2, 'outcome': b /
                    (a + b), 'pace': 2})

        for i in range(0, 5):
            a, b = multiple_generations_diffent_mew(
                initalpop, n, num, mr3)
            writer.writerow(
                {'population': num, 'mew': mr3, 'outcome': b /
                    (a + b), 'pace': 3})

        for i in range(0, 5):
            a, b = multiple_generations_diffent_mew(
                initalpop, n, num, mr4)
            writer.writerow(
                {'population': num, 'mew': mr4, 'outcome': b /
                    (a + b), 'pace': 4})

        for i in range(0, 5):
            a, b = multiple_generations_diffent_mew(
                initalpop, n, num, mr5)
            writer.writerow(
                {'population': num, 'mew': mr5, 'outcome': b /
                    (a + b), 'pace': 5})


makCSV(initalpop, 1000, 1000, 1, 10, 100, 1000, 10000)
