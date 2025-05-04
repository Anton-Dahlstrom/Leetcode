from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        hmap = defaultdict(int)
        res = 0
        for dom in dominoes:
            small = min(dom)
            big = max(dom)
            comb = (small, big)
            if hmap[comb]:
                res += hmap[comb]
            hmap[comb] += 1
        return res


dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
output = 3

obj = Solution()
res = obj.numEquivDominoPairs(dominoes)
print(res)
print(output)
print(res == output)
