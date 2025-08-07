class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        n = len(fruits[0])
        res = 0
        for i in range(n):
            res += fruits[i][i]
            fruits[i][i] = 0

        limit = (n-1)//2+1
        psize = 0
        size = 1
        inc = 1
        for i in range(1, n-1):
            if i == limit:
                inc = -1
                if not n % 2:
                    size -= inc
            psize = size
            size += inc
            for j in range(n-size, n):
                temp = 0
                for k in range(max(j-1, n-psize), min(j+2, n)):
                    temp = max(temp, fruits[i-1][k])
                fruits[i][j] += temp

            fruits[i][i] = 0
            for j in range(n-size, n):
                temp = 0
                for k in range(max(j-1, n-psize), min(j+2, n)):
                    temp = max(temp, fruits[k][i-1])
                fruits[j][i] += temp

        return res + fruits[n-1][n-2] + fruits[n-2][n-1]


fruits = [[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]]
output = 100


obj = Solution()
res = obj.maxCollectedFruits(fruits)
print(res)
print(output)
print(res == output)
