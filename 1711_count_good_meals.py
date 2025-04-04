
from typing import Counter


class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        deliciousness = Counter(deliciousness)
        MOD = 10**9+7
        res = 0
        powers = set()
        power = 2
        maxpower = 2**40+1
        while power < maxpower:
            powers.add(power)

            power <<= 1
        for val in deliciousness:
            if val in powers and 0 in deliciousness:
                res += deliciousness[val] * deliciousness[0]
                res %= MOD
            bits = val.bit_length()
            nextpow = 1 << bits
            needed = nextpow - val
            if val == needed:
                res += ((deliciousness[val]-1) * deliciousness[val])//2
            elif needed in deliciousness:
                res += (deliciousness[val] * deliciousness[needed])
            res %= MOD
        return res


deliciousness = [149, 107, 1, 63, 0, 1, 6867, 1325,
                 5611, 2581, 39, 89, 46, 18, 12, 20, 22, 234]
output = 12

obj = Solution()
res = obj.countPairs(deliciousness)
print(res)
print(output)
print(res == output)
