class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        cur = 0
        res = []
        for num in nums:
            cur <<= 1
            if num:
                cur += 1
            res.append(cur % 5 == 0)

        return res


nums = [0, 1, 1]
output = [True, False, False]

obj = Solution()
res = obj.prefixesDivBy5(nums)
print(res)
print(output)
print(res == output)
