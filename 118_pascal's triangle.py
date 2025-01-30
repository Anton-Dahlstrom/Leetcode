class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        for level in range(0, numRows-1):
            cur = [1]
            parent = res[level]
            for i in range(1, len(parent)):
                cur.append(parent[i-1] + parent[i])
            cur.append(1)
            res.append(cur)

        return res


numRows = 5
output = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

obj = Solution()
res = obj.generate(numRows)
print(res)
print(output)
print(res == output)
