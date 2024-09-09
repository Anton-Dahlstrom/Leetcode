class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Loops forever if there is one negative number and it's absolute
        # value is smaller than the positive value.

        def addTwoPositive(n1, n2):
            oldKeep = a ^ b
            shift = (a & b) << 1
            while shift:
                newKeep = oldKeep ^ shift
                shift = (oldKeep & shift) << 1
                oldKeep = newKeep
            return oldKeep

        def removeSmallNegative(large, small):
            # Keep whatever was removed from large before we find the first bit
            # in small.
            # If we remove 4 from 8 we keep everything below 8 except 2 and 1
            # 8 - 4 = 1000 - 0100 = 0100
            # 8 = 2 = 1000 - 0010 = 0110
            # 16-4 = 10000 - 00100 = 01100
            small = abs(small)

        if (a < 0 and 0 < b):
            if abs(a) < b:
                removeSmallNegative(b, a)

        if (b < 0 and 0 < a):
            if abs(b) < a:
                removeSmallNegative(a, b)
        return addTwoPositive(a, b)


a = 9
b = 7
output = 16

a = -19
b = 17
output = -2

a = -5
b = 8
output = 3

# a = -5
# b = -3
# output = -8

obj = Solution()
res = obj.getSum(a, b)
print(res)
print(res == output)
