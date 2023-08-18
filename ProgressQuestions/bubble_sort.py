def countSwaps(a):
    # Write your code here
    b = []
    count = 0
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                sorted = False
                a[i], a[i+1] = a[i+1], a[i]
                count += 1
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().strip().split()))

    countSwaps(a)
