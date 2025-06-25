class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return nums[-1]
        return nums[-3]


nums = [3, 2, 1]
output = 1

obj = Solution()
res = obj.thirdMax(nums)
print(res)
print(output)
print(res == output)
