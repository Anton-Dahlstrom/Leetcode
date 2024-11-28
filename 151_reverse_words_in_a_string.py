class Solution:
    def reverseWords(self, s: str) -> str:
        test = s.split(" ")
        res = []
        for word in reversed(test):
            if word:
                res.append(word)
        return " ".join(res)

s = " hello my  name is anton  "
output = "anton is name my hello"

obj = Solution()
res = obj.reverseWords(s)
print(output)
print(res)
print(res == output)