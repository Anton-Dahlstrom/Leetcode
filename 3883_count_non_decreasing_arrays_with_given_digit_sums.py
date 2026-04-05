class Solution:
    def countArrays(self, digitSum: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(digitSum)
        nums = [[] for _ in range(51)]
        for thousand in range(5):
            for hundred in range(10):
                for ten in range(10):
                    for one in range(10):
                        dsum = thousand + hundred + ten + one
                        nums[dsum].append(thousand * 1000 +
                                          hundred * 100 + ten * 10 + one)
        nums[5].append(5000)

        prevdigit = digitSum[0]
        dp = [1 for i in range(len(nums[prevdigit]))]
        for i in range(1, n):
            if not dp:
                return 0
            digit = digitSum[i]
            temp = [0]*len(nums[digit])
            pointer = 0
            cur = 0
            for i in range(len(nums[digit])):
                while pointer < len(dp) and nums[prevdigit][pointer] <= nums[digit][i]:
                    cur += dp[pointer]
                    pointer += 1
                temp[i] = cur % MOD
            dp = temp
            prevdigit = digit
        return sum(dp) % MOD
