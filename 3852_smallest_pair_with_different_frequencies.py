from typing import Counter


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        nums = list(set(nums))
        nums.sort()
        for i in range(len(nums)):
            num = nums[i]
            for key in nums[i+1:]:
                if key == num:
                    continue
                if cnt[num] != cnt[key]:
                    return [num, key]
        return [-1, -1]


nums = [1, 1, 2, 2, 3, 4]
output = [1, 3]

obj = Solution()
res = obj.minDistinctFreqPair(nums)
print(res)
print(output)
print(res == output)
