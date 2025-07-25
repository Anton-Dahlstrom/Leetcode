import heapq


class Solution:
    def halveArray(self, nums: list[int]) -> int:
        start = 0
        n = len(nums)
        for i in range(n):
            start += nums[i]
            nums[i] *= -1
        heapq.heapify(nums)
        res = 0
        cur = start
        half = start/2
        while cur > half:
            res += 1
            val = heapq.heappop(nums) / 2
            cur += val
            heapq.heappush(nums, val)
        return res


nums = [5, 19, 8, 1]
output = 3

obj = Solution()
res = obj.halveArray(nums)
print(res)
print(output)
print(res == output)
