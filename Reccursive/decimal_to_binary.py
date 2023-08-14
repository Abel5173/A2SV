def decimal_to_binary(n, binary):
    if n == 0:
        return binary
    result = str(n % 2) + binary
    return decimal_to_binary(n // 2, result)

n = 23
binary = ''
print(decimal_to_binary(n, binary))
