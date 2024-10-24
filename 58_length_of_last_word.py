class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


s = "luffy is still joyboy"
output = 6


obj = Solution()
res = obj.lengthOfLastWord(s)
print(res)
print(output)
print(res == output)
