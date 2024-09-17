class Solution:
    def getSum(self, a: int, b: int) -> int:

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

            def removeCommonBits(large, small):
                common = large & small
                large = large ^ common
                small = small ^ common
                return (large, small)

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
                temp = count
                while temp:
                    leftover <<= 1
                    temp >>= 1
                # Creates a binary sequence with all 1's that is one bit larger than
                # the range we are looking for.
                while count:
                    start <<= 1
                    start = start | base
                    count >>= 1
                # for _ in range(count):
                #     start <<= 1
                #     start = start | base
                # Removes the original True bit
                start = start ^ leftover
                # Keeps the bits that are True in the number input in the function.
                res = start & num
                return res

            base = 1
            while small:
                large, small = removeCommonBits(large, small)
                if not small:
                    return large
                shifts = shiftsToFirstBit(small)
                temp = shifts
                while temp:
                    small >>= 1
                    temp >>= 1
                temp = shifts
                while temp:
                    small <<= 1
                    temp >>= 1

                keeping = bitsInInterval(large, shifts)
                temp = shifts
                while temp:
                    large >>= 1
                    temp >>= 1
                shiftsToLargeBit = shiftsToFirstBit(large)
                shiftsToLargeBit >>= 1
                temp = shiftsToLargeBit
                while temp:
                    large >>= 1
                    temp >>= 1
                # Adds all 1's before the bit we removed
                # shiftsToLargeBit <<= 1
                while shiftsToLargeBit:
                    large <<= 1
                    large = large | base
                    shiftsToLargeBit >>= 1
                # Adds all 0's after the bit we removed
                shifts >>= 1
                while shifts:
                    large <<= 1
                    shifts >>= 1
                # Adds back the 1's after the bit we removed
                # large >>= 1
                large = large | keeping
            return large

        # If a is negative and smaller than b.
        if (a < 0 and 0 < b):
            if abs(a) <= b:
                return removeSmallNegative(b, a)

        # If b is negative and smaller than a.
        elif (b < 0 and 0 < a):
            if abs(b) <= a:
                return removeSmallNegative(a, b)
        return addTwoPositive(a, b)


a = 9
b = 7
output = 16

# a = -19
# b = 17
# output = -2

# a = -5
# b = 8
# output = 3

a = -14
b = 16
output = 2

# a = -1
# b = 1
# output = 0

a = -500
b = 750
output = 250

obj = Solution()
res = obj.getSum(a, b)
print(res)
print(res == output)
