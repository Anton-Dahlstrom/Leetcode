class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        bits = bin(n)[2:]
        arr = [int(num) for num in bits]
        length = len(arr)
        res = 0
        needed = 0
        for i in range(length):
            if arr[i] == needed:
                needed = 0
            else:
                needed = 1
                res += 2**(length-i-1)
        return res


n = 333
output = 393


obj = Solution()
res = obj.minimumOneBitOperations(n)
print(res)
print(output)
print(res == output)
