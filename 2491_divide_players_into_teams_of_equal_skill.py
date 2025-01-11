class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        s = sum(skill)
        cap = s//(len(skill)//2)
        avail = {}
        res = 0
        for n in skill:
            pair = cap-n
            if pair in avail:
                avail[pair] -= 1
                if avail[pair] == 0:
                    avail.pop(pair)
                res += n*pair
            else:
                avail.setdefault(n, 0)
                avail[n] += 1
        if avail:
            return -1
        return res


skill = [3, 2, 5, 1, 3, 4]
output = 22

skill = [2, 3, 4, 2, 5, 5]
output = 32

obj = Solution()
res = obj.dividePlayers(skill)
print(res)
print(output)
print(res == output)
