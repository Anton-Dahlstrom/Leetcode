class Solution:
    def maxSumDistinctTriplet(self, x: list[int], y: list[int]) -> int:
        n = len(x)
        y = [(y[i], i) for i in range(n)]
        y.sort(reverse=True)
        used = set()
        res = 0
        needed = 3
        for i in range(n):
            val, index = y[i]
            index = x[index]
            if index not in used:
                used.add(index)
                res += val
                needed -= 1
            if not needed:
                break
        if needed:
            return -1
        return res


x = [1, 2, 1, 3, 2]
y = [5, 3, 4, 6, 2]
output = 14

obj = Solution()
res = obj.maxSumDistinctTriplet(x, y)
print(res)
print(output)
print(res == output)
