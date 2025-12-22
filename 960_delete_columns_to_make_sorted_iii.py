from sortedcontainers import SortedList


class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        rows, cols = len(strs), len(strs[0])
        # observations:
        # 1<2 && 2<3 = 1<3
        # if we check what can be after each row and store the best as dp[i]
        # dp[i] = max(dp[i+1:])+1

        def isValidComboOfCols(left, right):
            for row in range(rows):
                if strs[row][left] > strs[row][right]:
                    return False
            return True

        dp = [0]*cols
        dp[cols-1] = 1
        sortedList = SortedList()
        sortedList.add((1, cols-1))
        for i in range(cols-2, -1, -1):  # left col
            best = (1, i)
            for j in range(len(sortedList)-1, -1, -1):
                if isValidComboOfCols(i, sortedList[j][1]):
                    best = (sortedList[j][0]+1, i)
                    break
            sortedList.add(best)
        return cols - sortedList[-1][0]


strs = ["babca", "bbazb"]
output = 3


obj = Solution()
res = obj.minDeletionSize(strs)
print(res)
print(output)
print(res == output)
