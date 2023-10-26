def findAnagrams(s: str, p: str):
        p = sorted(p)
        l = 0
        r = len(p)
        ans = []
        while r <= len(s):
            if sorted(s[l:r]) == p:
                ans.append(l)
            l += 1
            r += 1
        
        return ans

print(findAnagrams("abab", "ab"))