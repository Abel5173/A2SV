import decimal


while True:
    try:
        a, b, c = map(int, input().split())
        result = decimal.Decimal(a)/decimal.Decimal(b)
        print("{:.cf}".format(result))
    except EOFError:
        break
