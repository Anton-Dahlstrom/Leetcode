class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9+7
        n = len(corridor)
        totalSeats = 0
        openSeats = 0
        res = 1
        cur = 0
        for i in range(n):
            # try to place between i and i-1
            if corridor[i] == "S":
                if openSeats == 2:
                    res = res * cur % MOD
                    cur = 0
                    openSeats = 0
                totalSeats += 1
                openSeats += 1
            if openSeats == 2:
                cur += 1

        if totalSeats < 2 or totalSeats % 2:
            return 0
        if totalSeats == 2:
            return 1
        return res


corridor = "SSPPSPS"
output = 3


obj = Solution()
res = obj.numberOfWays(corridor)
print(res)
print(output)
print(res == output)
