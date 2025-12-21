class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        rows, cols = len(strs), len(strs[0])
        res = 0
        sortedRows = set()
        for col in range(cols):
            tempSorted = set()
            valid = True
            for row in range(1, rows):
                if row in sortedRows:
                    continue
                if strs[row-1][col] < strs[row][col]:
                    tempSorted.add(row)
                elif strs[row-1][col] > strs[row][col]:
                    res += 1
                    valid = False
                    break
            if valid:
                sortedRows.update(tempSorted)
        return res


strs = ["xga",
        "xfb",
        "yfa"]
output = 1


obj = Solution()
res = obj.minDeletionSize(strs)
print(res)
print(output)
print(res == output)
