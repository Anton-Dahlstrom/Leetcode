from collections import defaultdict


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        res = 0
        maximum = 0
        hmap = defaultdict(int)
        for num in nums:
            hmap[num] += 1
            if hmap[num] == maximum:
                res += 1
            elif hmap[num] > maximum:
                maximum = hmap[num]
                res = 1
        return maximum*res


nums = [1, 2, 2, 3, 1, 4]
output = 4

obj = Solution()
res = obj.maxFrequencyElements(nums)
print(res)
print(output)
print(res == output)
