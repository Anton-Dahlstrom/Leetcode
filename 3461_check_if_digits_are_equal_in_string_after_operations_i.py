class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = [int(c) for c in s]
        while len(arr) > 2:
            temp = []
            for i in range(len(arr)-1):
                temp.append((arr[i] + arr[i+1]) % 10)
            arr = temp
        return arr[0] == arr[1]


s = "34789"
output = False

s = "3902"
output = True

s = "323"
output = True

obj = Solution()
res = obj.hasSameDigits(s)
print(res)
print(output)
print(res == output)
