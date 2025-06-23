from typing import Counter


class Solution:
    def checkPrimeFrequency(self, nums: list[int]) -> bool:
        n = 101
        count = Counter(nums)
        primes = [True]*n
        primes[0], primes[1] = False, False
        for i in range(2, n):
            j = i
            while j <= n-i:
                j += i
                primes[j] = False
        for key in count:
            if primes[count[key]]:
                return True
        return False


nums = [1, 2, 3, 4, 5, 4]
output = True

nums = [2, 2, 2, 2, 2, 2, 2, 2, 2]
output = False

obj = Solution()
res = obj.checkPrimeFrequency(nums)
print(res)
print(output)
print(res == output)
