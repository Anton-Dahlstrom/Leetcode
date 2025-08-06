from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        start = -1
        for i in range(n):
            if nums[i] == k:
                start = i
        if start < 0:
            return 0

        left = defaultdict(int)
        right = defaultdict(int)
        cur = 0
        for i in range(start, n):
            if nums[i] > k:
                cur += 1
            elif nums[i] < k:
                cur -= 1
            right[cur] += 1

        cur = 0
        for i in range(start, -1, -1):
            if nums[i] > k:
                cur += 1
            elif nums[i] < k:
                cur -= 1
            left[cur] += 1
        res = 0
        for key in right:
            res += right[key] * left[key*-1]
            if key >= 0 and key+1 in right:
                res += right[key+1] * left[key*-1]
            if key <= 0:
                res += right[key] * left[(key*-1)+1]
        return res


nums = [3, 2, 1, 4, 5]
k = 4
output = 3


obj = Solution()
res = obj.countSubarrays(nums, k)
print(res)
print(output)
print(res == output)
