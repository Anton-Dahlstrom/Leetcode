class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        numstring = self.countAndSay(n-1)
        print(numstring)
        res = ""
        cur = ""
        count = 0
        for char in numstring:
            if char == cur:
                count += 1
            else:
                res += str(count) + cur
                cur = char
                count = 0

        if count:
            res += str(count) + cur
        return res
    
n = 4
output = "1211"

obj = Solution()
res = obj.countAndSay(n)
print(res)
print(output)
print(res == output)