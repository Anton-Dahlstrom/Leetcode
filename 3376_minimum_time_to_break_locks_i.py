from collections import deque


class Solution:
    def findMinimumTime(self, strength: list[int], k: int) -> int:
        queue = deque(strength)

        def dfs(time, x, arr: deque):
            if not arr:
                return time
            res = float("inf")
            for i in range(len(arr)):
                cur = arr.pop()
                inc = cur // x
                if cur % x:
                    inc += 1
                res = min(res, dfs(time+inc, x+k, arr))
                arr.appendleft(cur)
            return res
        return dfs(0, 1, queue)


strength = [3, 4, 1]
k = 1
output = 4

strength = [2, 5, 4]
k = 2
output = 5

strength = [7, 3, 6, 18, 22, 50]
k = 4
output = 12

obj = Solution()
res = obj.findMinimumTime(strength, k)
print(res)
print(output)
print(res == output)
