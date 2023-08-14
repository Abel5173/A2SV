def sumOfNaturalNumbers(n):
    if n <= 1:
        return n
    return n + sumOfNaturalNumbers(n - 1)

n = 10
print(sumOfNaturalNumbers(n))