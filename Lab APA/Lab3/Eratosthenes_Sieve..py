#Andrei Ceban FAF-211

import math
import time
import matplotlib.pyplot as plt


# Algorithm 1 -------------------------------------------------------
def algorithm_1(n):
    primes1 = []
    list1 = [True] * (n + 1)  # puneam toate elementele din lista markate(True)
    list1[0] = list1[1] = False  # primele 2 elemente le punem (False) astfel vom incepe de la indexul 2

    i = 2
    while (i <= n):
        if (list1[i] == True):
            j = 2 * i
            while (j <= n):
                list1[j] = False
                j = j + i
        i = i + 1

    for i in range(n + 1):
        if list1[i]:
            primes1.append(i)
    return primes1


# Algorithm 2 -------------------------------------------------------
def algorithm_2(n):
    primes2 = []
    list2 = [True] * (n + 1)  # puneam toate elementele din lista markate(True)
    list2[0] = list2[1] = False  # primele 2 elemente le punem (False) astfel vom incepe de la indexul 2

    i = 2
    while (i <= n):
        j = 2 * i
        while (j <= n):
            list2[j] = False
            j = j + i
        i = i + 1

    for i in range(n + 1):
        if list2[i]:
            primes2.append(i)
    return primes2


#Algorithm 3 -------------------------------------------------------
def algorithm_3(n):
    primes3 = []
    list3 = [True] * (n + 1)  # puneam toate elementele din lista markate(True)
    list3[0] = list3[1] = False  # primele 2 elemente le punem (False) astfel vom incepe de la indexul 2

    i = 2
    while (i <= n):
        if (list3[i] == True):
            j = i + 1
        while (j <= n):
            if (j % i == 0):
                list3[j] = False
            j = j + 1
        i = i + 1

    for i in range(n + 1):
        if list3[i]:
            primes3.append(i)
    return primes3


#Algorithm 4 -------------------------------------------------------
def algorithm_4(n):
    primes4 = []
    list4 = [True] * (n + 1)  # puneam toate elementele din lista markate(True)
    list4[0] = list4[1] = False  # primele 2 elemente le punem (False) astfel vom incepe de la indexul 2

    i = 2
    while (i <= n):
        j = 2
        while (j < i):
            if (i % j == 0):
                list4[i] = False
            j = j + 1
        i = i + 1

    for i in range(n + 1):
        if list4[i]:
            primes4.append(i)
    return primes4


#Algorithm 5 -------------------------------------------------------
def algorithm_5(n):
    primes5 = []
    list5 = [True] * (n + 1)  # puneam toate elementele din lista markate(True)
    list5[0] = list5[1] = False  # primele 2 elemente le punem (False) astfel vom incepe de la indexul 2

    i = 2
    while i <= n:
        j = 2
        while j <= math.sqrt(i):
            if i % j == 0:
                list5[i] = False
            j = j + 1
        i = i + 1

    for i in range(n + 1):
        if list5[i]:
            primes5.append(i)
    return primes5


#calculeaza timp de executie
def calc_time(func, params):
    start_time = time.time()
    func(params)
    end_time = time.time()
    return end_time - start_time

def plot_all_graph():
    algorithms = [algorithm_1, algorithm_2, algorithm_3, algorithm_4, algorithm_5]
    sizes = range(50, 1500, 100)

    for i, algorithm in enumerate(algorithms):
        times = []
        for size in sizes:
            times.append(calc_time(algorithm, size))
        plt.plot(sizes, times, label=f'algorithm_{i+1}')
    plt.legend()
    plt.xlabel('Input values')
    plt.ylabel('Execution Time in seconds')
    plt.show()

def plot_each_graph():
    algorithms = [algorithm_1, algorithm_2, algorithm_3, algorithm_4, algorithm_5]
    sizes = range(50, 1500, 100)

    for i, algorithm in enumerate(algorithms):
        times = []
        for size in sizes:
            times.append(calc_time(algorithm, size))
        plt.plot(sizes, times, label=f'algorithm_{i+1}', color="red")
        plt.legend()
        plt.xlabel('Input values')
        plt.ylabel('Execution Time in seconds')
        plt.show()

# Testare : -----------------------------------------------------
# plot_all_graph() # Afisare grafice impreuna
# plot_each_graph() # Afisare grafice separat

# Afisarea rezultat la fiecare algoritm
print("Algoritmul 1 : ",algorithm_1(10))
print("Algoritmul 2 : ",algorithm_2(20))
print("Algoritmul 3 : ",algorithm_3(30))
print("Algoritmul 4 : ",algorithm_4(40))
print("Algoritmul 5 : ",algorithm_5(50))




