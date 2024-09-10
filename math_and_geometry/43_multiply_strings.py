class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int1 = 0
        int2 = 0
        for i, char in enumerate(num1):
            val = (ord(char) - 48) * (10 ** (len(num1) - 1 - i))
            int1 += val
        for i, char in enumerate(num2):
            val = (ord(char) - 48) * (10 ** (len(num2) - 1 - i))
            int2 += val
        return str(int1 * int2)

num1 = "9"
num2 = "99"
output = "891"

print(output)
obj = Solution()
res = obj.multiply(num1, num2)
print(res)
print(res == output)