from math import comb


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        turns = minutesToTest//minutesToDie
        # how many buckets can be checked with dp[turn][pigs]
        dp = [[1, i+1] for i in range(turns+1)]
        pigs = 1

        while dp[turns][-1] < buckets:
            pigs += 1
            for turn in range(turns+1):
                if not turn:
                    dp[turn].append(1)
                    continue
                cur = 0
                for pigCount in range(pigs+1):
                    pigComb = comb(pigs, pigCount)
                    cur += dp[turn-1][pigs-pigCount]*pigComb
                dp[turn].append(cur)
        return pigs


buckets = 1000
minutesToDie = 15
minutesToTest = 60
output = 5

obj = Solution()
res = obj.poorPigs(buckets, minutesToDie, minutesToTest)
print(res)
print(output)
print(res == output)
