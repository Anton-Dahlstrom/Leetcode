class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            cur = 0
            while nums[i]:
                cur += nums[i] % 10
                nums[i] //= 10

            if cur == i:
                return i
        return -1


nums = [1, 10, 11]
output = 1

obj = Solution()
res = obj.smallestIndex(nums)
print(res)
print(output)
print(res == output)
