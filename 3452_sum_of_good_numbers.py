class Solution:
    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums = nums
        res = 0
        for i in range(n):
            if i - k >= 0:
                if nums[i-k] >= nums[i]:
                    continue
            if i+k < n:
                if nums[i+k] >= nums[i]:
                    continue
            res += nums[i]
        return res


nums = [1, 3, 2, 1, 5, 4]
k = 2
output = 12

obj = Solution()
res = obj.sumOfGoodNumbers(nums, k)
print(res)
print(output)
print(res == output)
