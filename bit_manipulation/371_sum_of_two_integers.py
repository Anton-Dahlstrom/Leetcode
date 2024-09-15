# add function to find all bits below the first subtracted bit and add them after removing everything below subtracting bit.
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
            small = abs(small)
            # First we found how far we have to shift to find the bit we need to remove:
            # Returns how many times you need to shift to find the first bit.

            def shiftsToFirstBit(num):
                compare = num
                shift = num
                count = 1
                while True:
                    shift >>= 1
                    shift <<= 1
                    count <<= 1
                    if shift == compare and shift > 0:
                        shift >>= 1
                        compare >>= 1
                        continue
                    break
                count >>= 1
                return count

            # Returns all the bits in a given amount of shifts.
            # Not returning correct result, input of 8 and 2 should return 1 but returns 2.
            def bitsInInterval(num, count):
                count = 2
                if count == 1:
                    return 0
                compare = num
                shift = num
                base = 1
                res = 1
                print("count", count, num)
                while count:
                    print(count)
                    count >>= 1
                    shift >>= 1
                    shift <<= 1
                    res <<= 1
                    if shift != compare:
                        res = res | base
                        continue
                    shift >>= 1
                    compare >>= 1
                res >>= 1
                print(bin(res))
                return res

            print(small, large)

            shifts = shiftsToFirstBit(small)
            print(shifts, "Shifts to first bit we remove")
            shifts2 = bitsInInterval(large, shifts)
            print(
                shifts2, "Bits we need to keep because they are smaller than the bit we are removing")
            # Keep whatever was removed from large before we find the first bit
            # in small.
            # If we remove 4 from 8 we keep everything below 8 besides except
            # for the values below the value we removed (in this case 4 so 2 and 1).
            # 8 - 4 = 1000 - 0100 = 0100
            # 8 = 2 = 1000 - 0010 = 0110
            # 16-4 = 10000 - 00100 = 01100

        # If a is negative and smaller than B.
        if (a < 0 and 0 < b):
            if abs(a) < b:
                return removeSmallNegative(b, a)

        # If b is negative and msaller than B
        elif (b < 0 and 0 < a):
            if abs(b) < a:
                return removeSmallNegative(a, b)
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
