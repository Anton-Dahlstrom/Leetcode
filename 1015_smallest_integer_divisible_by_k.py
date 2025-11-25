class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        cur = 0
        states = set()
        res = 0
        while True:
            cur *= 10
            cur += 1
            cur %= k
            res += 1
            if cur in states:
                return -1
            if not cur:
                break
            states.add(cur)

        return res


k = 3
output = 3

obj = Solution()
res = obj.smallestRepunitDivByK(k)
print(res)
print(output)
print(res == output)
