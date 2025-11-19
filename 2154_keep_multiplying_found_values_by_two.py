class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        nums = set(nums)
        while original in nums:
            original *= 2
        return original


nums = [5, 3, 6, 1, 12]
original = 3
output = 24

obj = Solution()
res = obj.findFinalValue(nums, original)
print(res)
print(output)
print(res == output)
