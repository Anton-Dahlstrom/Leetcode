from collections import defaultdict


class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        n = len(nums)
        dominant = -1
        hmap = defaultdict(int)
        for num in nums:
            hmap[num] += 1
            if hmap[num] > (n//2):
                dominant = num
        rcount = hmap[dominant]
        lcount = 0
        for i in range(n):
            if nums[i] == dominant:
                lcount += 1
                rcount -= 1
            lsize = i+1
            rsize = n-i-1
            if lcount > lsize//2 and rcount > rsize//2:
                return i

        return -1


nums = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]
output = 4

obj = Solution()
res = obj.minimumIndex(nums)
print(res)
print(output)
print(res == output)
