

def isPrime(number):
    for i in range(2, number):
       if number % i == 0:
           return False
    return True


def Nth_Prime(n):
    primeNumbers = []
    value = 2
    while len(primeNumbers) < n:
        if isPrime(value):
            primeNumbers.append(value)
        value += 1
    return primeNumbers[-1]


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors