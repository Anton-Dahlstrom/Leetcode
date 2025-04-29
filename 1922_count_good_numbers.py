class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = int((10**9) + 7)
        res = 0
        even = n//2
        odd = even
        if n % 2:
            odd += 1
        res += pow(4, even, MOD)
        res *= pow(5, odd, MOD)
        return res % MOD


n = 4
output = 400

obj = Solution()
res = obj.countGoodNumbers(n)
print(res)
print(output)
print(res == output)
