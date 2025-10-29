from collections import defaultdict


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if nums[i] == k:
                res += 1
        cnt = defaultdict(int)
        left = 0
        right = res
        for i in range(n):
            if nums[i] == k:
                left += 1
                right -= 1
            else:
                cnt[nums[i]] = max(left+1, cnt[nums[i]]+1)
                res = max(res, cnt[nums[i]]+right)

        return res


nums = [10, 2, 3, 4, 5, 5, 4, 3, 2, 2]
k = 10
output = 4

obj = Solution()
res = obj.maxFrequency(nums, k)
print(res)
print(output)
print(res == output)
