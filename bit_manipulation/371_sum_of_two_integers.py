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
            # Removes common bits
            small = abs(small)
            common = large & small
            large = large ^ common
            small = small ^ common
            if not small:
                return large

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

            # Returns all the bits in a given range of shifts.
            def bitsInInterval(num, count):
                base = 1
                start = 1
                leftover = 1
                leftover <<= count
                # Creates a binary sequence with all 1's that is one bit larger than
                # the range we are looking for.
                for _ in range(count):
                    start <<= 1
                    start = start | base
                # Removes the original True bit
                start = start ^ leftover
                # Keeps the bits that are True in the number input in the function.
                res = start & num
                return res

            print(small, large)
            while small:
                shifts = shiftsToFirstBit(small)
                print(shifts, "Shifts to first bit we remove")
                shifts2 = bitsInInterval(large, shifts)
                print(
                    shifts2, "Bits we need to keep because they are smaller than the bit we are removing")
                break
            # 8-4=4 1000 - 0100 = 0100
            # 8-2=6 1000 - 0010 = 0110
            # 16-2=14 = 10000 - 00010 = 01110
            # 8 - 5 = 3 = 1000 - 0101 = 0111 - 0100 = 0011

        # If a is negative and smaller than b.
        if (a < 0 and 0 < b):
            if abs(a) < b:
                return removeSmallNegative(b, a)

        # If b is negative and smaller than a.
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

obj = Solution()
res = obj.getSum(a, b)
print(res)
print(res == output)
