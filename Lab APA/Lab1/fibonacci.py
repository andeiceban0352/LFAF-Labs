import time
import math
import matplotlib.pyplot as plt

#Algoritmul recursiv
def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

#Dynamic programing
def fib2(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

#Algoritmul iterativ
def fib3(n):
    a = 0
    b = 1
    if n < 0:
        print("Enter a number greater than 0")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

# Matrix
def fib4(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]

def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F, n):
    M = [[1, 1],
         [1, 0]]

    for i in range(2, n + 1):
        multiply(F, M)

#Binet’s formula
def fib5(n):
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))



def fib6(n):
    MAX = 1000
    f = [0] * MAX

    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        f[n] = 1
        return (f[n])

    # If fib(n) is already computed
    if (f[n]):
        return f[n]

    if (n & 1):
        k = (n + 1) // 2
    else:
        k = n // 2

    if ((n & 1)):
        f[n] = (fib6(k) * fib6(k) + fib6(k - 1) * fib6(k - 1))
    else:
        f[n] = (2 * fib6(k - 1) + fib6(k)) * fib6(k)

    return f[n]


def draw(n,F):
    x = list(range(n))
    y = []
    t = []
    for i in range(n):
        start_time = time.time()
        F(i)
        end_time = time.time()
        y.append(F(i))
        t.append(end_time - start_time)

    plt.plot(x, t)
    plt.xlabel("n-th Fibonacci Term")
    plt.ylabel("Time (s)")
    plt.title("Binet’s  Fibonacci Function")
    plt.show()

def printTable(n,F):
    max_value = F(n - 1)
    num_digits = len(str(max_value))
    max_width = max(4, num_digits)
    if n < 0:
        print("n should be > 0")
    else:
        for i in range(n):
            print("{:^{}}".format(i + 1, max_width), end="|")
        print("\n", end="")
        for i in range(n):
            print("{:^{}}".format(F(i), max_width), end="|")
        print("\n", end="")
        for i in range(n):
            start_time = time.time()
            F(i)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("{:^{}.2f}".format(elapsed_time, max_width), end="|")
        draw(n,F)


n = int(input("Enter the n: "))
printTable(n,fib3)