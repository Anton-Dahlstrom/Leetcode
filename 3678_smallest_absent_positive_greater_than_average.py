from statistics import mean


class Solution:
    def smallestAbsent(self, nums: list[int]) -> int:
        exists = set(nums)
        average = mean(nums)
        i = max(1, int(average) + 1)
        while i in exists:
            i += 1
        return i


nums = [-1, 1, 2]
output = 3

obj = Solution()
res = obj.smallestAbsent(nums)
print(res)
print(output)
print(res == output)
