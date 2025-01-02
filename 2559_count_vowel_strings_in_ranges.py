class SparseTableSum():

    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.log = [0] * (self.n+1)
        self.buildLog()
        self.k = self.log[-1] + 1
        self.table = self.buildSparseTable()

    def buildLog(self):
        for i in range(2, self.n+1):
            self.log[i] = self.log[i//2]+1

    def buildSparseTable(self):
        table = [[0] * self.k for _ in range(self.n)]
        for i in range(self.n):
            table[i][0] = self.arr[i]

        for j in range(1, self.k):
            i = 0
            while i + (1 << j) <= self.n:
                table[i][j] = table[i][j-1] + table[i + (1 << (j-1))][j-1]
                i += 1
        return table

    def query(self, left, right):
        ans = 0
        for j in range(self.k, -1, -1):
            if (left + (1 << j) - 1 <= right):
                ans += self.table[left][j]
                left += 1 << j
        return ans


class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = {"a", "e", "i", "o", "u"}
        ans = [0]*len(queries)
        words = [1 if (w[0] in vowels and w[-1] in vowels)
                 else 0 for w in words]
        table = SparseTableSum(words)
        for i, query in enumerate(queries):
            ans[i] = table.query(query[0], query[1])
        return ans


words = ["bzmxvzjxfddcuznspdcbwiojiqf", "mwguoaskvramwgiweogzulcinycosovozppl", "uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs", "uivcdsboxnraqpokjzaayedf", "yalc", "bbhlbmpskgxmxosft", "vigplemkoni", "krdrlctodtmprpxwditvcps", "gqjwokkskrb", "bslxxpabivbvzkozzvdaykaatzrpe", "qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi",
         "siqbezhkohmgbenbkikcxmvz", "ddmaireeouzcvffkcohxus", "kjzguljbwsxlrd", "gqzuqcljvcpmoqlnrxvzqwoyas", "vadguvpsubcwbfbaviedr", "nxnorutztxfnpvmukpwuraen", "imgvujjeygsiymdxp", "rdzkpk", "cuap", "qcojjumwp", "pyqzshwykhtyzdwzakjejqyxbganow", "cvxuskhcloxykcu", "ul", "axzscbjajazvbxffrydajapweci"]
queries = [[4, 4], [6, 17], [10, 17], [9, 18], [17, 22], [5, 23], [2, 5], [17, 21], [
    5, 17], [4, 8], [7, 17], [16, 19], [7, 12], [9, 20], [13, 23], [1, 5], [19, 19]]
output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

obj = Solution()
res = obj.vowelStrings(words, queries)
print(res)
print(output)
print(res == output)
