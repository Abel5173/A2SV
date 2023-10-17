s = "ababcbacadefegdehijhklij"
op = []
dic = {}
for key, val in enumerate(s):
    dic[val] = key
print(dic)
start = 0
end = 0
for key, val in enumerate(s):
    end = max(end, dic[val])
    if key == end:
        op.append(end - start + 1)
        start = end + 1
print(op)