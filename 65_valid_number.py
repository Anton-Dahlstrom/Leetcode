# Formally, a valid number is defined using one of the following definitions:

# An integer number followed by an optional exponent.
# A decimal number followed by an optional exponent.
# An integer number is defined with an optional sign '-' or '+' followed by digits.

# A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

# Digits followed by a dot '.'.
# Digits followed by a dot '.' followed by digits.
# A dot '.' followed by digits.
# An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

# The digits are defined as one or more digits.
class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        nums = []
        split = False
        for i in range(len(s)):
            if s[i] == "e" or s[i] == "E":
                if split:
                    return False
                nums.append(s[i:])
                nums.append(s[:i])
                if next:
                    nums.append(next)
                split = True

        # if prevSplit < len(s)-1 or not nums:
        #     nums.append(s[prevSplit:])
        print(nums)
        for num in nums:
            print(num)
            i = 0
            period = False
            if num[0] == "-" or num[0] == "+":
                i += 1
            if num[i] == '.':
                if not i < len(num)-1:
                    return False
                period = True
                i += 1
            while i < len(num):
                if not str.isnumeric(num[i]):
                    print(num[i] == ".", period)
                    if num[i] == "." and not period:
                        period = True
                    else:
                        return False
                i += 1
        return True


s = "3e0"
output = False

obj = Solution()
res = obj.isNumber(s)
print(res)
print(output)
print(res == output)
