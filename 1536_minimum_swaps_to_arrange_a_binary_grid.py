from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        res = 0
        arr = [0]*n
        for row in range(n):
            for col in range(n-1,-1,-1):
                if grid[row][col] == 1:
                    arr[row] = col
                    break

        for i in range(n):
            found = False
            for j in range(i,n):
                if arr[j] <= i:
                    res += j-i
                    arr = [arr[j]] + arr[:j] + arr[j+1:]
                    found = True
                    break
            if not found:
                return -1

        return res
