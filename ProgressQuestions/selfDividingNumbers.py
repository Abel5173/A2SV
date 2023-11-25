def selfDividingNumbers(left, right):
    result = []
    for i in range(left, right+1):
        k = str(i)
        b = True
        for j in k:
            if j == '0':
                b = False
                break
            elif i % int(j) == 0:
                continue
            else:
                b = False
                break
        if b:
            result.append(i)
    
    return result

print(selfDividingNumbers(1, 22))
