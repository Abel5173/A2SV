class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for path in paths:
            k = path.split(" ")
            l = []
            for i in range(1, len(k)):
                t = k[i].split("(")
                if t[1] in d:
                    d[t[1]].append(f'{k[0]}/{t[0]}')  
                else:
                    d[t[1]] = [f'{k[0]}/{t[0]}'] 
        
        l =[]
        for i in d.values():
            if len(i)>1:
                l.append(i)
                
        print(l)
        return l