class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        arr = [float("inf")]*(n+1)
        arr[0] = 0
        for i in range(1, n+1):
            for j in range(1, 4):
                if i - j < 0:
                    break
                arr[i] = min(arr[i], (j**2)+arr[i-j])
            arr[i] += costs[i-1]
        return arr[-1]


n = 4
costs = [5, 1, 6, 2]
output = 11

obj = Solution()
res = obj.climbStairs(n, costs)
print(res)
print(output)
print(res == output)
