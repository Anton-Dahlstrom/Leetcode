class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9+7
        diff = 6
        same = 6
        for i in range(n-1):
            tempDiff = ((same*2)+(diff*2)) % MOD
            tempSame = ((same*3)+(diff*2)) % MOD
            diff = tempDiff
            same = tempSame
        return (diff+same) % MOD


n = 5000
output = 30228214

obj = Solution()
res = obj.numOfWays(n)
print(res)
print(output)
print(res == output)
