### Number Theory Concepts for Competitive Programming:

#### Prime Numbers and Primality Testing:

```python
# Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n+1) if primes[i]]

# Miller-Rabin Primality Test
import random

def is_prime_miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as (2^r * d) + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
```

#### Modular Arithmetic:

```python
# Modular Exponentiation
def modular_exponentiation(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result
```

#### GCD and LCM:

```python
# Euclidean Algorithm for GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# LCM using GCD
def lcm(a, b):
    return (a * b) // gcd(a, b)
```

#### Euler's Totient Function:

```python
# Euler's Totient Function (φ)
def euler_totient_function(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result
```

#### Chinese Remainder Theorem (CRT):

```python
# Chinese Remainder Theorem
def chinese_remainder_theorem(a, m):
    total_prod = 1
    for mod in m:
        total_prod *= mod

    result = 0
    for ai, mi in zip(a, m):
        bi = total_prod // mi
        result += ai * pow(bi, -1, mi) * bi

    return result % total_prod
```

#### Fermat's Little Theorem:

```python
# Fermat's Little Theorem
def fermat_little_theorem(a, p):
    return pow(a, p - 1, p) == 1
```

#### Number Bases and Digits:

```python
# Base Conversion
def base_conversion(number, base_from, base_to):
    return int(str(number), base_from), str(number, base_to)

# Extract Digits
def extract_digits(number):
    return [int(digit) for digit in str(number)]

# Reverse Digits
def reverse_digits(number):
    return int(str(number)[::-1])
```

#### Divisibility Rules:

```python
# Divisibility by 2
def is_divisible_by_2(number):
    return number % 2 == 0

# Divisibility by 3
def is_divisible_by_3(number):
    return sum(int(digit) for digit in str(number)) % 3 == 0

# Divisibility by 4
def is_divisible_by_4(number):
    return int(str(number)[-2:]) % 4 == 0

# Divisibility by 5
def is_divisible_by_5(number):
    return str(number)[-1] in {'0', '5'}

# Divisibility by 9
def is_divisible_by_9(number):
    return sum(int(digit) for digit in str(number)) % 9 == 0

# Divisibility by 11
def is_divisible_by_11(number):
    odd_sum = 0
    even_sum = 0
    for i, digit in enumerate(str(number)):
        if i % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    return abs(odd_sum - even_sum) % 11 == 0
```

#### Exponentiation by Squaring:

```python
# Exponentiation by Squaring
def exponentiation_by_squaring(base, exponent):
    if exponent == 0:
        return 1
    if exponent % 2 == 1:
        return base * exponentiation_by_squaring(base, exponent - 1)
    half_result = exponentiation_by_squaring(base, exponent // 2)
    return half_result * half_result
```

#### Diophantine Equations:

```python
# Solving Linear Diophantine Equations
def solve_diophantine(a, b, c):
    g = gcd(a, b)
    if c % g != 0:
        return None
    x, y = extended_gcd(a, b)
    factor = c // g
    return x * factor, y * factor
```

#### Farey Sequences:

```python
# Generating Farey Sequence
def farey_sequence(n):
    farey = [(0, 1), (1, 1)]
    for denominator in range(2, n+1):
        for numerator in range(1, denominator):
            if gcd(numerator, denominator) == 1:
                farey.append((numerator, denominator))
    farey.sort(key=lambda x: x[0] / x[1])
    return farey
```

#### Prime Factorization:

```python
# Prime Factorization
def prime_factorization(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors
```
