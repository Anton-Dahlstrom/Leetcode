class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        powers = []
        i = 0
        while True:
            val = 1 << i
            if val > n:
                break
            if val & n:
                powers.append(val)
            i += 1

        for i in range(1, len(powers)):
            powers[i] *= powers[i-1]

        res = []
        for query in queries:
            start, stop = query
            val = powers[stop]
            if start > 0:
                val //= powers[start-1]
            val %= 1000000007
            res.append(val)
        return res


n = 15
queries = [[0, 1], [2, 2], [0, 3]]
output = [2, 4, 64]

obj = Solution()
res = obj.productQueries(n, queries)
print(res)
print(output)
print(res == output)
