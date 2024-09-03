class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


digits = [1, 2, 3]
output = [1, 2, 4]

digits = [9, 9, 9]
output = [1, 0, 0, 0]

obj = Solution()
res = obj.plusOne(digits)
print(res)
print(res == output)
