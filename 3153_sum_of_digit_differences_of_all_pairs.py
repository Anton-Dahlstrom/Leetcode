class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        count = [0]*10
        while nums[0]:
            for i in range(n):
                count[nums[i] % 10] += 1
                nums[i] //= 10
            for i in range(10):
                for j in range(i+1, 10):
                    res += count[i] * count[j]
                count[i] = 0
        return res


nums = [13, 23, 12]
output = 4


obj = Solution()
res = obj.sumDigitDifferences(nums)
print(res)
print(output)
print(res == output)
