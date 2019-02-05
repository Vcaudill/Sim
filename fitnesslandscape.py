import math
import matplotlib.pyplot as plt
import numpy as np
from math import e
from math import pi
import matplotlib.patches as mpatches

poppopnum = 1000
loci = locus = 10
opfit = (loci / 2)
repoduction = 50
inver_mutation_rate = 1000
rate = 1
genend = 1000
sigma = (.25 * loci)
value = 0
num = 0
value = math.exp(-math.pow(
    -(num - opfit), 2) / (2 * (math.pow(sigma, 2))))
# num is really genotype[i] = count, all the ones from 0 to # of loci
print(list(range(0, loci + 1)))
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

num = np.arange(0., loci + 1., 1)
print(value)
#plt.plot(num, value, 'r--')

'''
def graph(value, num):
    x = np.array(num)
    y = eval(value)
    plt.plot(x, y)
    plt.show()
'''


def graph(formula, x_range, color):
    x = np.array(x_range)
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y, color)


# graph(math.exp(-math.pow(-(num - opfit), 2) / (2 * (math.pow(sigma, 2)))),
#      list(range(0, loci + 1)))


graph(lambda x: e**(-((x - opfit)**2) / (2 * (.25 * loci)**2)), range(0, 11), 'blue')
graph(lambda x: e**(-((x - opfit)**2) / (2 * (.5 * loci)**2)), range(0, 11), 'red')
graph(lambda x: e**(-((x - opfit)**2) / (2 * (.75 * loci)**2)), range(0, 11), 'green')
graph(lambda x: e**(-((x - opfit)**2) / (2 * (.1 * loci)**2)), range(0, 11), 'orange')
graph(lambda x: e**(-((x - opfit)**2) / (2 * (1 * loci)**2)), range(0, 11), 'yellow')
graph(lambda x: e**(-((x - opfit)**2) / (2 * (.15 * loci)**2)), range(0, 11), 'purple')

plt.title('Fitness Lanscape Sigma Test')
plt.xlabel('Phenotype')
plt.ylabel('Fitness')
blue = mpatches.Patch(color='blue', label='.25 * loci')
red = mpatches.Patch(color='red', label='.5 * loci')
green = mpatches.Patch(color='green', label='.75 * loci')
orange = mpatches.Patch(color='orange', label='.1 * loci')
yellow = mpatches.Patch(color='yellow', label='1 * loci')
purple = mpatches.Patch(color='purple', label='.2 * loci')

plt.legend(handles=[orange, purple, blue, red, green, yellow]).draggable()
path = "/Users/victoria/Desktop/Sim/"
folder = "Sigma_TEST_Fitness_burnin/"
mypath = path + folder
graph_file = "".join([mypath, '/graph' + ".pdf"])
plt.savefig(graph_file)
plt.show()


'''
For this to work I need sb= 0.1,0.01 and sd = -0.01, -.001
move optfit by one from 0 to 1?
individulas with 4 will first be 0.1 then change to -0.01 after fitness change


num = 0
opfit = 1
value = math.exp(-math.pow(-(num - opfit), 2) / (2 * (math.pow(sigma, 2))))
print(value)


if indivial is opfit then assign it a fitness value of the sd
if not at opfit can you assign it the sd
then it goes into locus (0,1) to pick the next generation
'''
