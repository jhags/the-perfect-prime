

def check_inputs(func):
    def wrapper(value):
        if value <= 1:
            raise Exception("The input value must be greater than 1")
        return func(value)
    return wrapper


def isPrime(number):
    """Check if a number is prime.

    Args:
        number (int or float): a number to test.

    Returns:
        Bool: True if prime, False if not.
    """
    if number <= 1:
        return False

    for i in range(2, number):
       if number % i == 0:
           return False
    return True


def n_primes(n):
    if n < 1:
        raise Exception("n must be greater than or equal to 1")

    primeNumbers = []
    value = 2
    while len(primeNumbers) < n:
        if isPrime(value):
            primeNumbers.append(value)
        value += 1
    return primeNumbers


def nth_prime(n):
    primeNumbers = n_primes(n)
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
