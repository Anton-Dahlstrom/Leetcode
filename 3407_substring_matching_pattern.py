class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        if len(p) == 1:
            return True
        if len(p)-1 > len(s):
            return False
        left, right = p.split("*")
        if not right:
            if left in s:
                return True
        l = 0
        for l in range(len(s)):
            if l+len(left) >= len(s):
                return False
            if s[l:l+len(left)] == left:
                if right in s[l + len(left):]:
                    return True
                break
        return False


s = "xks"
p = "s*"
output = True

obj = Solution()
res = obj.hasMatch(s, p)
print(res)
print(output)
print(res == output)
