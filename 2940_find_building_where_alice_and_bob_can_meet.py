class SparseTableMin:

    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.log = [0] * (self.n+1)
        self.buildLog()
        self.table = self.buildSparseTable()

    def buildLog(self):
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i//2]+1

    def buildSparseTable(self):
        k = self.log[self.n] + 1
        table = [[0]*k for _ in range(self.n)]

        for i in range(self.n):
            table[i][0] = self.arr[i]

        for j in range(1, k):
            i = 0
            while i + (1 << j) <= self.n:
                table[i][j] = max(
                    table[i][j - 1], table[i + (1 << (j - 1))][j - 1])
                i += 1

        return table

    def query(self, left, right):
        length = right - left + 1
        j = self.log[length]
        return max(self.table[left][j], self.table[right - (1 << j) + 1][j])


class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        res = []
        table = SparseTableMin(heights)
        for query in queries:
            i, j = query
            i, j = min(i, j), max(i, j)
            if heights[j] > heights[i] or i == j:
                res.append(j)
                continue
            target = max(heights[i], heights[j])
            l = j+1
            r = len(heights) - 1
            if l > r:
                if heights[j] > heights[i]:
                    res.append(j)
                else:
                    res.append(-1)
                continue
            if table.query(l, r) <= target:
                res.append(-1)
                continue
            while l < r:
                mid = l + ((r-l)//2)
                if table.query(l, mid) > target:
                    r = mid - 1
                    if table.query(l, r) <= target:
                        l = mid
                        break
                else:
                    l = mid + 1
            res.append(l)
        return res


heights = [460930928, 800206458, 406221516, 367069516, 36015176,
           811477961, 975343880, 552354186, 32421554]
queries = [[0, 2], [7, 1], [2, 4], [2, 0], [
    7, 3], [1, 1], [4, 2], [4, 7], [4, 3], [6, 1]]

output = [5, -1, 5, 5, 7, 1, 5, 7, 5, 6]
obj = Solution()
res = obj.leftmostBuildingQueries(heights, queries)
print(res)
print(output)
print(res == output)
