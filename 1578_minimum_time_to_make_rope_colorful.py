class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        n = len(colors)
        res = 0
        curmax = neededTime[0]
        for i in range(1, n):
            if colors[i] == colors[i-1]:
                if neededTime[i] > curmax:
                    res += curmax
                    curmax = neededTime[i]
                else:
                    res += neededTime[i]
            else:
                curmax = neededTime[i]

        return res


colors = "abaac"
neededTime = [1, 2, 3, 4, 5]
output = 3

colors = "bbbaaa"
neededTime = [4, 9, 3, 8, 8, 9]
output = 23

obj = Solution()
res = obj.minCost(colors, neededTime)
print(res)
print(output)
print(res == output)
