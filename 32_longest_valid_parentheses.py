class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = []
        space = -1

        for i in range(0, len(s)):
            if s[i] == "(":
                if space < 0:
                    space = 0
                space += 1
                if space > len(stack):
                    stack.append(i)
            else:
                space -= 1
                if space < 0:
                    if stack:
                        stack.pop()
                    continue
                if space < len(stack)-1:
                    stack.pop()
                val = stack[-1]
                distance = i - val + 1
                res = max(res, distance)
        return res


s = ")()())()()("
output = 4

obj = Solution()
res = obj.longestValidParentheses(s)
print(res)
print(output)
print(res == output)
