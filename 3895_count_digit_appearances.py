class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        target = str(digit)
        res = 0
        for num in nums:
            for chr in str(num):
                if chr == target:
                    res += 1
        return res
