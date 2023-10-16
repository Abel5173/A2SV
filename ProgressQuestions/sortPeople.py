names = ["IEO","Sgizfdfrims","QTASHKQ","Vk","RPJOFYZUBFSIYp","EPCFFt","VOYGWWNCf","WSpmqvb"]
heights = [17233,32521,14087,42738,46669,65662,43204,8224]

for i in range(len(names)):
    min_value = 0
    for j in range(i, len(names)):
        if heights[j] > min_value:
            min_value = heights[j]
            print(min_value)
    idx = heights.index(min_value)
    names[i], names[idx] = names[idx], names[i]
    heights[i], heights[idx] = heights[idx], heights[i]

print(names)
['EPCFFt', 'RPJOFYZUBFSIYp', 'VOYGWWNCf', 'Vk', 'Sgizfdfrims', 'IEO', 'QTASHKQ', 'WSpmqvb']
["EPCFFt","RPJOFYZUBFSIYp","VOYGWWNCf","Vk","Sgizfdfrims","IEO","QTASHKQ","WSpmqvb"]