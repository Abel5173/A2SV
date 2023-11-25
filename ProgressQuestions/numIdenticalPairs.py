def numIdenticalPairs(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    result = 0
    for i in dic:
        if dic[i] > 1:
            result += ((dic[i] * (dic[i] - 1)//2))

    return result

print(numIdenticalPairs([1,2,3,1,1,3]))