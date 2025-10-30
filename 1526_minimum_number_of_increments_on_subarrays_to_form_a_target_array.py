class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        n = len(target)
        res = 0
        prev = 0
        for i in range(n):
            res += max(0, target[i]-prev)
            prev = target[i]
        return res


target = [3, 1, 5, 4, 2]
output = 7

obj = Solution()
res = obj.minNumberOperations(target)
print(res)
print(output)
print(res == output)
