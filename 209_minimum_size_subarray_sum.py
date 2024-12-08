class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0
        res = 0
        l = 0
        r = 0
        cur = nums[0]
        while True:
            if cur >= target:
                if not res:
                    res = r - l + 1
                else:
                    res = min(res, r-l+1)
                cur -= nums[l]
                l += 1
                if l >= len(nums):
                    return res
                if l > r:
                    r = l
                    cur += nums[r]
            else:
                r += 1
                if r >= len(nums):
                    return res
                cur += nums[r]


target = 7
nums = [2, 3, 1, 2, 4, 3]
output = 2

obj = Solution()
res = obj.minSubArrayLen(target, nums)
print(res)
print(output)
print(res == output)
