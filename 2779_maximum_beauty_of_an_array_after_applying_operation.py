class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        res = 1
        l = 0
        r = 1
        ran = range(nums[l], nums[l]+(k*2)+1)
        while r < len(nums):
            if nums[r] in ran:
                r += 1
                res = max(res, r-l)
            else:
                l += 1
                ran = range(nums[l], nums[l]+(k*2)+1)
        return res


nums = [4, 6, 1, 2]
k = 2
output = 3


obj = Solution()
res = obj.maximumBeauty(nums, k)
print(res)
print(output)
print(res == output)
