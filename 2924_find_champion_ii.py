class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        # Can't create single connected graph with all teams
        if len(edges) < n-1:
            return -1
        if n == 1:
            return 0

        winners = set()
        losers = set()
        for edge in edges:
            winner, loser = edge[0], edge[1]
            if loser in winners:
                winners.remove(loser)
            losers.add(loser)
            if winner not in losers:
                winners.add(winner)

        if len(winners) == 1 and len(winners) + len(losers) == n:
            return winners.pop()
        return -1

n = 4
edges = [[0,2],[1,3],[1,2]]
output = -1

# n = 3
# edges = [[0,1],[1,2]]
# output = 0

n = 1
edges = []
output = 0

obj = Solution()
res = obj.findChampion(n, edges)
print(res)
print(output)
print(res == output)