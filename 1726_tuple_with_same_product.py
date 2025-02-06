from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        n = len(nums)
        products = defaultdict(int)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                val = nums[i] * nums[j]
                products[val] += 1
                if products[val] > 1:
                    res += 8 * (products[val]-1)
        return res


nums = [1, 2, 4, 5, 10]
output = 16

nums = [2, 3, 4, 6]
output = 8

obj = Solution()
res = obj.tupleSameProduct(nums)
print(res)
print(output)
print(res == output)
