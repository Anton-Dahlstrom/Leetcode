class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = 0
        l = 0
        r = 0
        cursum = 0
        while l < n:
            while r < n and (cursum+nums[r]) * (r-l+1) < k:
                cursum += nums[r]
                r += 1
            res += r-l
            cursum -= nums[l]
            l += 1
        return res


nums = [2, 1, 4, 3, 5]
k = 10
output = 6

obj = Solution()
res = obj.countSubarrays(nums, k)
print(res)
print(output)
print(res == output)
