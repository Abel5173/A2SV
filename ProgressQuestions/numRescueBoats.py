class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        cnt = 0
        li = []
        while l < r:
            if people[l] == limit:
                cnt += 1
                li.append(people[l])
            if people[r] == limit:
                cnt += 1
                li.append(people[r])
            if people[l] + people[r] > limit:
                r -= 1
            elif people[l] + people[r] <= limit:
                li.append(people[l])
                li.append(people[r])
                cnt += 1
                l += 1
                r -= 1
        
        return cnt + (len(people)-len(li))
