class Solution:
    def maximumLength(self, s: str) -> int:
        hmap = {}
        res = 0
        for i, char in enumerate(s):
            hmap.setdefault(char,[]).append(i)
        for key in hmap:
            rounds = 0
            cur = hmap[key]
            while len(cur) >= 3:
                temp = []
                for i in range(len(cur)):
                    if cur[i] < len(s) - 1 and s[cur[i]+1] == key:
                        temp.append(cur[i]+1)
                rounds += 1
                cur = temp
            res = max(res, rounds)
        if not res:
            return -1
        return res


s = "abcaba"
output=  1

s = "aaaa"
output = 2

obj = Solution()
res = obj.maximumLength(s)
print(res)
print(output)
print(res == output)