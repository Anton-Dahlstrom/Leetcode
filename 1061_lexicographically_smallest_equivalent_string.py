class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        def union(i, j):
            ipar = find(i)
            jpar = find(j)
            minpar = min(ipar, jpar)
            parent[ipar] = minpar
            parent[jpar] = minpar
            return parent[i]

        def find(i):
            if parent[i] == i:
                return i
            return find(parent[i])

        parent = [i for i in range(26)]
        for i in range(len(s1)):
            c1, c2 = ord(s1[i]) - 97, ord(s2[i]) - 97
            union(c1, c2)

        res = []
        for c in baseStr:
            res.append(chr(find(ord(c)-97)+97))
        return "".join(res)


s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"
output = "aauaaaaada"


obj = Solution()
res = obj.smallestEquivalentString(s1, s2, baseStr)
print(res)
print(output)
print(res == output)
