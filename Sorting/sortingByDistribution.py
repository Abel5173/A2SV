# Types of sorting by distribution: Counting, Radix, Bucket
# Counting Sort: O(n + k) time | O(n + k) space
# Code:
def countingSort(array):
    k = max(array) + 1
    count = [0] * k
    for i in array:
        count[i] += 1
    for i in range(1, k):
        count[i] += count[i-1]
    output = [0] * len(array)
    for i in reversed(array):
        output[count[i]-1] = i
        count[i] -= 1
    return output

# Radix Sort: O(d(n + b)) time | O(n + b) space
# Code:
def radixSort(array):
    maxNum = max(array)
    exp = 1
    while maxNum / exp > 0:
        countingSortByDigit(array, exp)
        exp *= 10
    return array
def countingSortByDigit(array, exp):
    k = 10
    count = [0] * k
    for i in array:
        count[(i//exp)%10] += 1
    for i in range(1, k):
        count[i] += count[i-1]
    output = [0] * len(array)
    for i in reversed(array):
        output[count[(i//exp)%10]-1] = i
        count[(i//exp)%10] -= 1
    for i in range(len(array)):
        array[i] = output[i]

# Bucket Sort: O(n + k) time | O(n + k) space
# Code:
def bucketSort(array):
    numberOfBuckets = 3
    maxNum = max(array)
    size = maxNum / numberOfBuckets
    buckets = [[] for _ in range(numberOfBuckets)]
    for i in array:
        buckets[int(i/size)].append(i)
    for i in range(numberOfBuckets):
        insertionSort(buckets[i])
    output = []
    for i in range(numberOfBuckets):
        output += buckets[i]
    return output
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

# Explanation of sorting by distribution:
# Counting Sort: Count the number of elements with distinct key values, 
# and use arithmetic to determine the position of each key value in the output sequence.
# Radix Sort: Sort the elements by first grouping the individual digits of the same place value.
# Then, sort the elements according to their increasing/decreasing order.
# Bucket Sort: Distribute the elements of an array into a number of buckets.
# Each bucket is then sorted individually, either using a different sorting algorithm,
# or by recursively applying the bucket sorting algorithm.


# More Explanation on Bucket Sort:
# Bucket sort is mainly useful when input is uniformly distributed over a range.
# For example, consider the following problem.
# Sort a large set of floating point numbers which are in range from 0.0 to 1.0 and are uniformly distributed across the range.
# How do we sort the numbers efficiently?
# A simple way is to apply a comparison based sorting algorithm.
# The lower bound for Comparison based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is Ω(n Log n),
# i.e., they cannot do better than nLogn.
# Can we sort the array in linear time? Counting sort can not be applied here as we use keys as index in counting sort.
# Here keys are floating point numbers.
# The idea is to use bucket sort.
# Following is bucket algorithm.
# bucketSort(arr[], n)
# 1) Create n empty buckets (Or lists).
# 2) Do following for every array element arr[i].
# .......a) Insert arr[i] into bucket[n*array[i]]
# 3) Sort individual buckets using insertion sort.
# 4) Concatenate all sorted buckets.
# The time complexity of bucket sort is O(n + k) with O(n) space.
# The space complexity can be reduced further by using linked lists instead of arrays to represent buckets.
# The space complexity of bucket sort is O(n).
# The main disadvantage of bucket sort is that it is not suitable for sorting large data sets.
