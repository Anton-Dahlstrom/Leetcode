class Solution:
    def reverse(self, x: int) -> int:
        xstr = str(x)
        reverse = xstr[::-1]
        if reverse[-1] == "-":
            val = int(reverse[:-1]) * -1
        else:
            val = int(reverse)
        if val not in range(-2**31-1, 2**31):
            return 0
        return val


x = -250
output = -52

obj = Solution()
res = obj.reverse(x)
print(output)
print(res)
print(res == output)
