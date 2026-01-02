class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        found = set()
        for num in nums:
            if num in found:
                return num
            found.add(num)


nums = [5, 1, 5, 2, 5, 3, 5, 4]
output = 5

obj = Solution()
res = obj.repeatedNTimes(nums)
print(res)
print(output)
print(res == output)
