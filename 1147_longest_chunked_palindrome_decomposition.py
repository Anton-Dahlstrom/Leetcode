class Solution:
    def longestDecomposition(self, text: str) -> int:
        N = len(text)
        l, r = 0, N-1
        lstr, rstr = "", ""
        res = 0
        while l < r:
            lstr += text[l]
            rstr = text[r] + rstr
            if lstr == rstr:
                res += 2
                lstr = ""
                rstr = ""
            l += 1
            r -= 1

        if lstr or len(text) % 2:
            res += 1
        return res


text = "ghiabcdefhelloadamhelloabcdefghi"
output = 7

obj = Solution()
res = obj.longestDecomposition(text)
print(res)
print(output)
print(res == output)
