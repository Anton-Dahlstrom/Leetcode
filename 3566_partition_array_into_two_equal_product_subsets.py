class Solution:
    def checkEqualPartitions(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        start = 1
        for num in nums:
            start *= num

        def dfs(i, p1, p2):
            if i == n:
                return False
            if p1 == target:
                if p2 == target:
                    return True
                return False
            val = nums[i]
            if dfs(i+1, p1 // val, p2 * val):
                return True
            if dfs(i+1, p1, p2):
                return True
            return False
        return dfs(0, start, 1)


nums = [3, 1, 6, 8, 4]
target = 24

output = True

obj = Solution()
res = obj.checkEqualPartitions(nums, target)
print(res)
print(output)
print(res == output)
