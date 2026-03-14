from typing import Counter


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 0 and cnt[nums[i]] == 1:
                return nums[i]
        return -1


nums = [3, 4, 2, 5, 4, 6]
output = 2
obj = Solution()
res = obj.firstUniqueEven(nums)
print(res)
print(output)
print(res == output)
