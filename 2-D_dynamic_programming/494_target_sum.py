class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        self.res = 0

        def dfs(i, val):
            if i < len(nums):
                dfs(i+1, val + nums[i])
                dfs(i+1, val - nums[i])
            elif i == len(nums) and val == target:
                self.res += 1

        dfs(0, 0)
        return self.res


nums = [1, 1, 1, 1, 1]
target = 3
output = 5

nums = [40, 19, 30, 48, 8, 50, 13, 31, 29,
        38, 35, 31, 40, 47, 7, 16, 31, 33, 45, 6]
target = 49


obj = Solution()
res = obj.findTargetSumWays(nums, target)
print(res)
print(res == output)
