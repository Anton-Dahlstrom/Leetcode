from collections import defaultdict


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        hmap = defaultdict(int)
        res = 0
        for ans in answers:
            hmap[ans] += 1
            if hmap[ans] == 1:
                res += ans+1
            if hmap[ans] > ans:
                hmap[ans] = 0
        return res


1

answers = [1, 1, 2]
output = 5

answers = [1, 0, 1, 0, 0]
output = 5

obj = Solution()
res = obj.numRabbits(answers)
print(res)
print(output)
print(res == output)
