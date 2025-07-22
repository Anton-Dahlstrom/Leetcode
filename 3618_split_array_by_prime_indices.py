class Solution:
    def splitArray(self, nums: list[int]) -> int:
        n = len(nums)
        primes = [True]*(n+1)
        primes[0], primes[1] = False, False
        primesum, nonprimesum = 0, 0
        for i in range(n):
            if primes[i]:
                primesum += nums[i]
            else:
                nonprimesum += nums[i]
            cur = i+i
            while i > 1 and cur < n:
                primes[cur] = False
                cur += i
        return abs(primesum - nonprimesum)


nums = [2, 3, 4]
output = 1

obj = Solution()
res = obj.splitArray(nums)
print(res)
print(output)
print(res == output)
