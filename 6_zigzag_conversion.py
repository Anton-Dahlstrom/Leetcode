class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        strings = [""]*numRows
        indexes = [i for i in range(numRows)]
        indexes += [i for i in range(numRows-2, 0, -1)]
        cur = 0
        for char in s:
            strings[indexes[cur]] += char
            cur += 1
            if cur >= len(indexes):
                cur = 0
        for substr in strings:
            res += substr
        return res


s = "PAYPALISHIRING"
numRows = 3
output = "PAHNAPLSIIGYIR"

obj = Solution()
res = obj.convert(s, numRows)
print(res)
print(output)
print(res == output)
