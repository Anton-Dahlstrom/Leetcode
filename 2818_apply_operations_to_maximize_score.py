class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        MOD = (10**9) + 7
        n = len(nums)
        m = max(nums)+1
        arr = [0] * m
        arr[0] = arr[1] = 1
        # Calculate primes
        for i in range(m//2+1):
            if arr[i]:
                continue
            for nonprime in range(i, m, i):
                arr[nonprime] += 1

        scores = [0] * n
        for i in range(n):
            val = nums[i]
            if val < 2:
                scores[i] = 0
            elif not arr[val]:
                scores[i] = 1
            else:
                scores[i] = arr[val]

        nextgreater = [0]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and scores[i] >= stack[-1][0]:
                stack.pop()
            if not stack:
                nextgreater[i] = n
            else:
                nextgreater[i] = stack[-1][1]
            stack.append((scores[i], i))

        prevgreater = [0]*n
        stack = []
        for i in range(n):
            while stack and scores[i] > stack[-1][0]:
                stack.pop()
            if not stack:
                prevgreater[i] = -1
            else:
                prevgreater[i] = stack[-1][1]
            stack.append((scores[i], i))

        nums = [(nums[i], i) for i in range(n)]
        nums.sort()
        res = 1
        while nums:
            val, i = nums.pop()
            l = prevgreater[i]+1
            r = nextgreater[i]-1
            leftsize = i-l+1
            rightsize = r-i+1
            totalsize = leftsize * rightsize
            res *= pow(val, min(totalsize, k), MOD)
            res %= MOD
            k -= totalsize
            if k <= 0:
                break
        return res


nums = [3289, 2832, 14858, 22011]
k = 6
output = 256720975


obj = Solution()
res = obj.maximumScore(nums, k)
print(res)
print(output)
print(res == output)
