class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


a = "1010"
b = "1011"
output = "10101"

obj = Solution()
res = obj.addBinary(a, b)
print(res)
print(output)
print(res == output)
