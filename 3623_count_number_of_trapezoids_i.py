from collections import defaultdict


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        MOD = 10**9 + 7
        rowCount = defaultdict(int)
        combinations = 0
        for x, y in points:
            rowCount[y] += 1
        for row in rowCount:
            num = rowCount[row]
            comb = int(((num-1)/2) * num)
            combinations += comb
            rowCount[row] = comb

        res = 0
        for key in rowCount:
            num = rowCount[key]
            combinations -= num
            res += num * combinations % MOD
        return res % MOD


points = [[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]
output = 3

obj = Solution()
res = obj.countTrapezoids(points)
print(res)
print(output)
print(res == output)
