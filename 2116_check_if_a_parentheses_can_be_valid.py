class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 or (s[0] == ")" and locked[0] == "1") or (s[-1] == "(" and locked[-1] == "1"):
            return False
        space = 0
        for i in range(len(s)):
            if s[i] == ")" and locked[i] == "1":
                if not space:
                    return False
                space -= 1
            else:
                space += 1
        space = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(" and locked[i] == "1":
                if not space:
                    return False
                space -= 1
            else:
                space += 1
        return True


s = "))()))"
locked = "010100"
output = True


obj = Solution()
res = obj.canBeValid(s, locked)
print(res)
print(output)
print(res == output)
