class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)

        def dfs(i, cur):
            res = 0
            for j in range(i, n):
                next = cur ^ nums[j]
                res += next
                res += dfs(j+1, next)
            return res

        return dfs(0, 0)


nums = [5, 1, 6]
output = 28

obj = Solution()
res = obj.subsetXORSum(nums)
print(res)
print(output)
print(res == output)
