class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Loops forever if there is one negative number and it's absolute
        # value is larger than the positive value.
        oldKeep = a ^ b
        shift = (a & b) << 1
        while shift:
            newKeep = oldKeep ^ shift
            shift = (oldKeep & shift) << 1
            oldKeep = newKeep
        return oldKeep


a = 9
b = 7
output = 16

a = -19
b = 17
output = -2

obj = Solution()
res = obj.getSum(a, b)
print(res)
print(res == output)
