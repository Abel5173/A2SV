# Let's say we want to build a frequency counter for items in the following array
arr = [1,2,3,1,2,3,4,1,2,1,4,1,2,3,1]

freq = {}

for item in arr:
  # Fetch a value of 0 in case the key doesn't exist. Otherwise, fetch the stored value
  freq[item] = freq.get(item, 0) + 1

print(freq)