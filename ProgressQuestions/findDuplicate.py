class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dp = {}
        for i in paths:
            path = i.split()
            for j in range(1, len(path)):
                file = path[j].split('(')
                if file[1] in dp:
                    dp[file[1]].append(path[0] + '/' + file[0])
                else:
                    dp[file[1]] = [path[0] + '/' + file[0]]