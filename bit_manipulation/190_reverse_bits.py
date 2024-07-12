class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)
        b = b[-1:1:-1]
        b = b + "0" * (32 - len(b))
        res = int(b, 2)
        return res


n = 43261596
output = 964176192

n = 4294967293
output = 3221225471

obj = Solution()
res = obj.reverseBits(n)
print(res)
print(res == output)
