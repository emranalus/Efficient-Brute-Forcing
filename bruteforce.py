from itertools import product
import timeit
import numpy as np


def calcRepeat(bit_length):
    # We have 2 tables their repeat is the calculated with bit_length / x
    # and there shouldn't be any leftovers bigger one goes to first table.
    counter = 1
    while True:
        counter += 1
        if bit_length % counter == 0:
            return int(bit_length / counter), counter


# Parameters
data = [0, 1]

repeat = calcRepeat(int(input("Length of bitstring: ")))
firstRepeat = max(repeat[0], repeat[1])
secondRepeat = min(repeat[0], repeat[1])

# Main Code
lst = np.array(list(product(np.array(data), repeat=firstRepeat)))

start = timeit.default_timer()
lst2 = list(product(lst, repeat=secondRepeat))
stop = timeit.default_timer()

print("---------------------")
print(lst2[-1])
print("---------------------")

print('Time: ', round(stop - start, 2), 'sec')
