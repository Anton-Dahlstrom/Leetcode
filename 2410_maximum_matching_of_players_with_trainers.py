class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        n = len(players)
        m = len(trainers)
        j = n-1
        res = 0
        for i in range(m-1, -1, -1):
            while j >= 0 and players[j] > trainers[i]:
                j -= 1
            if j < 0:
                break
            j -= 1
            res += 1
        return res


players = [4, 7, 9]
trainers = [8, 2, 5, 8]
output = 2

obj = Solution()
res = obj.matchPlayersAndTrainers(players, trainers)
print(res)
print(output)
print(res == output)
