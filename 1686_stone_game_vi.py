class Solution:
    def stoneGameVI(self, aliceValues: list[int], bobValues: list[int]) -> int:
        n = len(aliceValues)
        vals = [[0, i] for i in range(n)]
        for i in range(n):
            vals[i][0] = aliceValues[i] + bobValues[i]
        vals.sort(reverse=True)
        a, b = 0, 0
        for i in range(n):
            if i % 2 == 0:
                a += aliceValues[vals[i][1]]
            else:
                b += bobValues[vals[i][1]]
        if a > b:
            return 1
        elif a < b:
            return -1
        return 0


aliceValues = [2, 4, 3]
bobValues = [1, 6, 7]
output = -1

obj = Solution()
res = obj.stoneGameVI(aliceValues, bobValues)
print(res)
print(output)
print(res == output)
