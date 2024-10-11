class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        numstring = self.countAndSay(n-1)
        print(numstring)
        res = ""
        prev = ""
        count = 0
        for char in numstring+"f":
            if char == prev:
                count += 1
            else:
                if count:
                    res += str(count) + prev 
                prev = char
                count = 1

        return res
    
n = 4
output = "1211"

obj = Solution()
res = obj.countAndSay(n)
print(res)
print(output)
print(res == output)