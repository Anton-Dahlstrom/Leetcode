from collections import defaultdict


class Solution:
    def minLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = float("inf")
        hmap = defaultdict(int)
        l, r = 0, 0
        cursum = 0
        while r < n:
            if not hmap[nums[r]]:
                cursum += nums[r]
            hmap[nums[r]] += 1

            while cursum >= k and l < r:
                removing = 0
                left = nums[l]
                if hmap[left] == 1:
                    removing = left
                if cursum - removing >= k:
                    cursum -= removing
                    hmap[left] -= 1
                    l += 1
                else:
                    break
            r += 1
            if cursum >= k:
                res = min(res, r-l)

        if res == float("inf"):
            return -1
        return res


nums = [3, 2, 3, 4]
k = 5
output = 2


obj = Solution()
res = obj.minLength(nums, k)
print(res)
print(output)
print(res == output)
