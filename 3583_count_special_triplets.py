from collections import Counter, defaultdict


class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        MOD = 10**9+7
        prefix = defaultdict(int)
        suffix = Counter(nums)
        res = 0
        for num in nums:
            suffix[num] -= 1
            res += prefix[num*2] * suffix[num*2] % MOD
            res %= MOD
            prefix[num] += 1

        return res


nums = [8, 4, 2, 8, 4]
output = 2

obj = Solution()
res = obj.specialTriplets(nums)
print(res)
print(output)
print(res == output)
