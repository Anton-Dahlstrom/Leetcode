class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        res = 0
        rows, cols = len(strs), len(strs[0])
        for col in range(cols):
            for row in range(1, rows):
                if strs[row][col] < strs[row-1][col]:
                    res += 1
                    break

        return res


strs = ["cba", "daf", "ghi"]
output = 1

obj = Solution()
res = obj.minDeletionSize(strs)
print(res)
print(output)
print(res == output)
