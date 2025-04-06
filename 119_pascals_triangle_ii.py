class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        arr = [1]
        for row in range(1, rowIndex+1):
            size = len(arr)-1
            temp = [0] * (size)
            temp = [1] + temp + [1]

            for i in range(1, size+1):
                temp[i] = arr[i-1] + arr[i]
            arr = temp
        return arr


rowIndex = 3
output = [1, 3, 3, 1]


obj = Solution()
res = obj.getRow(rowIndex)
print(res)
print(output)
print(res == output)
