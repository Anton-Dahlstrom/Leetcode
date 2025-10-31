class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        found = set()
        res = []
        for num in nums:
            if num in found:
                res.append(num)
            found.add(num)
        return res


nums = [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]
output = [4, 5]

obj = Solution()
res = obj.getSneakyNumbers(nums)
print(res)
print(output)
print(res == output)
