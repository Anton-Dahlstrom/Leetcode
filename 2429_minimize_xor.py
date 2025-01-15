class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n1ones = bin(num1).count("1")
        n2ones = bin(num2).count("1")
        if n2ones == n1ones:
            return num1

        x = 0
        needed = n2ones
        extra = n2ones - n1ones
        i = 0
        while extra > 0:
            if 1 << i & num1 == 0:
                needed -= 1
                extra -= 1
                x += (1 << i)
            i += 1
        for i in range(len(bin(num1))-1, 0, -1):
            if 1 << (i-1) & num1:
                x += 1 << i-1
                needed -= 1
            if not needed:
                break
        return x


num1 = 25
num2 = 72
output = 24

obj = Solution()
res = obj.minimizeXor(num1, num2)
print(res)
print(output)
print(res == output)
