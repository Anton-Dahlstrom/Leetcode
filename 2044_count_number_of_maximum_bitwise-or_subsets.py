class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        n = len(nums)
        maxbits = 0
        for i in range(n):
            maxbits |= nums[i]

        def dfs(i, cur):
            res = 0
            if cur | nums[i] == maxbits:
                res += 1
            if i < n-1:
                res += dfs(i+1, cur)
                res += dfs(i+1, cur | nums[i])
            return res
        return dfs(0, 0)


nums = [3, 2, 1, 5]
output = 6

nums = [2, 2, 2]
output = 7

nums = [2, 2]
output = 3

obj = Solution()
res = obj.countMaxOrSubsets(nums)
print(res)
print(output)
print(res == output)
