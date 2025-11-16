class Solution:
    def numSub(self, s: str) -> int:
        MOD = (10**9)+7
        size = 0
        res = 0
        s += "0"
        for c in s:
            if c == "0":
                res += (size/2)*(size+1) % MOD
                size = 0
            else:
                size += 1
        return int(res)


s = "0110111"
output = 9

obj = Solution()
res = obj.numSub(s)
print(res)
print(output)
print(res == output)
