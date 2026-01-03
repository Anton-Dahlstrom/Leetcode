class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        start = s[0:k]
        start = start[::-1]
        end = s[k:]
        return start+end


s = "abcd"
k = 2
output = "bacd"

obj = Solution()
res = obj.reversePrefix(s, k)
print(res)
print(output)
print(res == output)
