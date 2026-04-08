from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        for l, r, k, v in queries:
            for i in range(l, r+1, k):
                nums[i] = nums[i] * v % MOD
        res = 0
        for i in range(n):
            res ^= nums[i]
        return res
