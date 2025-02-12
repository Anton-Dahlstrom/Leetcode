from collections import defaultdict


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        hmap = defaultdict(list)
        for num in nums:
            digitsum = 0
            for char in str(num):
                digitsum += int(char)
            hmap[digitsum].append(num)
        res = -1
        for key in hmap:
            if len(hmap[key]) > 1:
                hmap[key].sort()
                res = max(res, hmap[key][-1] + hmap[key][-2])

        return res


nums = [18, 43, 36, 13, 7]
output = 54

obj = Solution()
res = obj.maximumSum(nums)
print(res)
print(output)
print(res == output)
