class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        hmap = {}
        for row in matrix:
            zeroes = ""
            ones = ""
            for num in row:
                if num == 1:
                    zeroes += "0"
                    ones += "1"
                else:
                    zeroes += "1"
                    ones += "0"
            hmap[zeroes] = hmap.get(zeroes, 0) + 1
            hmap[ones] = hmap.get(ones, 0) + 1
        return max(hmap.values())


matrix = [[0, 0, 0],
          [0, 0, 1],
          [1, 1, 0]]
output = 2

obj = Solution()
res = obj.maxEqualRowsAfterFlips(matrix)
print(res)
print(output)
print(res == output)
