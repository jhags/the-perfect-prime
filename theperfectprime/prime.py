

def check_inputs(func):
    def wrapper(value):
        if value <= 1:
            raise Exception("The input value must be greater than 1.")
        return func(value)
    return wrapper


@check_inputs
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


@check_inputs
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