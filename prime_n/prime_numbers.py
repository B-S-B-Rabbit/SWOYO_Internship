"""
Модуль prime_numbers содержит функцию, реализующую алгоритм решета Эратосфена для поиска простых чисел в диапазоне.
"""
__author__ = 'Андрей Помошников'

from math import sqrt, ceil, trunc


def prime_numbers(low, high):
    if low > high or high < 2 or low < 0 or high - low == 0:
        return []
    high_sqrt = trunc(sqrt(high))
    MAX_SQRT = high_sqrt
    nprimes = [False] * (MAX_SQRT + 1)
    primes = []

    for i in range(3, high_sqrt + 1, 2):
        if not nprimes[i]:
            primes.append(i)
            for j in range(i ** 2, high_sqrt + 1, i):
                nprimes[j] = True

    if low % 2 == 0:
        low_n2 = low + 1
    else:
        low_n2 = low
    if high % 2 == 0:
        high_n2 = high - 1
    else:
        high_n2 = high
    low_n2 = max(3, low_n2)
    result = list(range(low_n2, high_n2 + 1, 2))
    length = len(result)
    for prime in primes:
        mod = low_n2 % prime
        if mod == 0:
            ind = 0
        elif (low_n2 + prime - mod) % 2 == 0:
            ind = round((prime + prime - mod) / 2)
        else:
            ind = round((prime - mod) / 2)
        if ind >= length:
            continue
        if result[ind] == prime:
            ind += prime
        result[ind::prime] = [0] * ceil((length - ind) / prime)
    return [2] + [i for i in result if i] if low < 2 else [i for i in result if i]