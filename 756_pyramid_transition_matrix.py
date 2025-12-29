from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        hmap = defaultdict(set)
        for s in allowed:
            hmap[s[:2]].add(s[2])

        def dfs(below, cur):
            if len(below) == 1:
                return True
            if len(below) == len(cur)+1:
                return dfs(cur, "")
            index = len(cur)
            bottomChars = below[index] + below[index+1]
            for next in hmap[bottomChars]:
                if dfs(below, cur+next):
                    return True
            return False
        return dfs(bottom, "")


bottom = "BCD"
allowed = ["BCC", "CDE", "CEA", "FFF"]
output = True

obj = Solution()
res = obj.pyramidTransition(bottom, allowed)
print(res)
print(output)
print(res == output)
