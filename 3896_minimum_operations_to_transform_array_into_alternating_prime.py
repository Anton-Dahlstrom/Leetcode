class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = 110001
        primes = [True]*n
        primes[0] = False
        primes[1] = False
        stack = []
        for i in range(2, n):
            if primes[i]:
                stack.append(i)
                for j in range(i+i, n, i):
                    primes[j] = False
        nums = [[nums[i], i % 2] for i in range(len(nums))]
        nums.sort()
        res = 0
        bigger = stack.pop()
        while nums:
            num, odd = nums.pop()
            if num == 2 and odd:
                res += 2
            elif odd and primes[num]:
                res += 1
            elif not odd and not primes[num]:
                while stack and stack[-1] > num:
                    bigger = stack.pop()
                dist = bigger-num
                res += dist
        return res
