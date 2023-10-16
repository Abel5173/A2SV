class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # i=0
        # j=-1
        # l=[]
        # skill.sort()
        # prev=skill[i]+skill[j]
        # sum=0
        # while i<len(skill)//2:
        #     if prev==skill[j]+skill[i]:
        #         sum+=skill[j]*skill[i]
        #     else:
        #         return -1
        #     i+=1
        #     j-=1
        # return sum
        l, r = 1, len(skill) - 2
        skill.sort()
        prev = skill[0] + skill[-1]
        sm = skill[0] * skill[-1]
        while l < r:
            if skill[l] + skill[r] != prev:
                return -1
            else:
                sm += (skill[l] * skill[r])
            l += 1
            r -= 1
        return sm


