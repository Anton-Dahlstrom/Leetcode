class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        query_row += 1
        row = 1
        cur = [poured]
        while row < query_row:
            row += 1
            temp = [0]*(row)
            for i in range(row):
                if i and cur[i-1] > 1:
                    temp[i] += (cur[i-1]-1)/2
                if i < row-1 and cur[i] > 1:
                    temp[i] += (cur[i]-1)/2
            cur = temp
        return min(1, cur[query_glass])
