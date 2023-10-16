arr = [7,3,5,2,6,8,1,9,4,3,7,3]
count = [0]*(max(arr) + 1)
ans = []
for num in arr:
    count[num] += 1
for i in range(len(count)):
    if count[i] != 0:
        ans.extend([i] * count[i])
# ans.extend
print(ans)