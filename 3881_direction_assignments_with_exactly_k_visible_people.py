import math


class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        MOD = 10**9+7
        return math.comb(n-1, k) * 2 % MOD
