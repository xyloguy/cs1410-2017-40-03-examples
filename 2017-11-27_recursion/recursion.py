import time
from sys import setrecursionlimit
setrecursionlimit(1002)


def factorial_loop(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)



start = time.time()
factorial_loop(1000)
end = time.time()
print(end - start)

start = time.time()
factorial_recursive(1000)
end = time.time()
print(end - start)