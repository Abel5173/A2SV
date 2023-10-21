class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        l,r = 0, 0
        cnt = 0
        players.sort()
        trainers.sort()
        while l < len(players) and r < len(trainers):
            if players[l] <= trainers[r]:
                cnt += 1
                l += 1
                r += 1
            else:
                r += 1
        
        return cnt