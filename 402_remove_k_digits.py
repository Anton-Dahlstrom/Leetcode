class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i = 0
        while i < len(num)-1 and k:
            if int(num[i]) > int(num[i+1]):
                num = num[:i] + num[i+1:]
                k -= 1
                i = max(0, i-1)
            else:
                i+=1
        if k:
            num = num[:len(num)-k]
        i = 0
        while i < len(num):
            if num[i] == "0":
                i+=1
            else:
                break
        num = num[i:]
        if not num:
            return "0"
        return num

num = "1432219"
k = 3
output= "1219"

num = "10"
k = 2

num = "1234567890"
k=9
output = "0"

num = "10001"
k = 4
output = "0"

obj = Solution()
res = obj.removeKdigits(num, k)
print(res)
print(output)
print(res == output)