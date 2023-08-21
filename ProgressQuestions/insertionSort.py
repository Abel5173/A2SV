def insertionSort(n, arr):
    x = arr[n-1]
    while n > 0 :
        if n == 1:
            arr[n-1] = x
            break
        if arr[n-2] < x:
            arr[n-1] = x
            break
        arr[n-1] = arr[n-2]
        n -= 1
    return arr
print(insertionSort(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]))
