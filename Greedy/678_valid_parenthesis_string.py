class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        wildcardL = 0
        wildcardR = 0
        for char in s:
            if char == '(':
                wildcardR = min(left, wildcardR)
                left += 1
            elif char == '*':
                wildcardL += 1
                if left:
                    wildcardR += 1
            else:
                if left > 0:
                    left -= 1
                elif wildcardL > 0:
                    wildcardL -= 1
                    wildcardR = max(wildcardR - 1, 0)
                else:
                    return False
        if left > wildcardR:
            return False
        return True


s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
output = False

s = "*)*())"
output = True


obj = Solution()
res = obj.checkValidString(s)
print(res)
print(res == output)
