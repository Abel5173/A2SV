# Types of sorting by comparison: Bubble, Selection, Insertion, Merge, Quick, Heap
# Bubble Sort: O(n^2) time | O(1) space
# Code:
def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False
        counter += 1
    return array
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# Selection Sort: O(n^2) time | O(1) space
# Code:
def selectionSort(array):
    for i in range(len(array)):
        smallestIdx = i
        for j in range(i+1, len(array)):
            if array[smallestIdx] > array[j]:
                smallestIdx = j
        swap(i, smallestIdx, array)
    return array
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# Insertion Sort: O(n^2) time | O(1) space
# Code:
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

arr = [8, 5, 2, 9, 5, 6, 3]
print(insertionSort(arr))

# Merge Sort: O(nlog(n)) time | O(nlog(n)) space
# Code:
def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))
def mergeSortedArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArray
# Quick Sort: O(nlog(n)) time | O(log(n)) space
# Code:
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array
def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(pivotIdx, rightIdx, array)
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
# Heap Sort: O(nlog(n)) time | O(1) space
# Code:
def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        siftDown(0, endIdx - 1, array)
    return array
def buildMaxHeap(array):
    firstParentIdx = (len(array) - 2) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)
def siftDown(currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap[idxToSwap] > heap[currentIdx]:
            swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
# Explaination of Sorting by Comparison
# # Sorting by Comparison is a technique that uses comparison to sort an array
# # Sorting by Comparison is used to sort an array by comparing each element in the array 
# to every other element in the array and swapping the elements if they are out of order

