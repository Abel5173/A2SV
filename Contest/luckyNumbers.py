def luckyNumber(n):
    count = 0
    isLucky = True
    for i in n:
        if i == '4' or i == '7':
            count += 1

    for i in str(count):
        if i != '4' and i != '7':
            isLucky = False
            break
    return isLucky

n = str(input())
if luckyNumber(n):
    print("YES")
else:
    print("NO")

    
    