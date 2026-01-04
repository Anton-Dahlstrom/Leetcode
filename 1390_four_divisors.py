class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        n = max(nums)+2
        divisible = [2]*(n)
        divsum = [i+1 for i in range(n)]
        for i in range(2, n):
            cur = i*2
            while cur < n:
                divsum[cur] += i
                divisible[cur] += 1
                cur += i

        res = 0
        for num in nums:
            if divisible[num] == 4:
                res += divsum[num]
        return res


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = 45

obj = Solution()
res = obj.sumFourDivisors(nums)
print(res)
print(output)
print(res == output)
