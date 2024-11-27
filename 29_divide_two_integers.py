class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        maxSize = 2147483647
        minSize = -2147483648
        positive = False
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            positive = True
        count = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        while count <= maxSize and count >= minSize:
            c = 1
            temp = divisor
            while temp <= dividend:
                temp <<= 1
                c <<= 1
            c >>= 1
            if not c:
                break
            temp >>= 1
            dividend -= temp
            if positive:
                count += c
            else:
                count -= c

        if positive:
            return min(maxSize, count)
        return max(minSize, count)


dividend = 10
divisor = 3
output = 3

obj = Solution()
res = obj.divide(dividend, divisor)
print(res)
print(output)
print(res == output)
