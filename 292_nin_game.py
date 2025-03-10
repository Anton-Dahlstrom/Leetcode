class Solution:
    def canWinNim(self, n: int) -> bool:
        if not n % 4:
            return False
        return True


n = 4
output = False

obj = Solution()
res = obj.canWinNim(n)
print(output)
print(res)
print(res == output)
