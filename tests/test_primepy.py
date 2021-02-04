import pytest

import theperfectprime as pp


def test_isPrime():
    assert pp.isPrime(0) is True
    assert pp.isPrime(2) is True
    assert pp.isPrime(15) is False

    assert pp.isPrime(1) is True
    assert pp.isPrime(3) is True
    assert pp.isPrime(7) is True


def test_Nth_Prime():
    # pp.Nth_Prime(0)
    assert pp.Nth_Prime(1) == 2
    assert pp.Nth_Prime(2) == 3


def test_prime_factors():
    assert pp.prime_factors(17) == [17]
    assert pp.prime_factors(100) == [2, 2, 5, 5]