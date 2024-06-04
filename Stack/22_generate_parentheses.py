n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]


class Solution:

    def generateParenthesis(self, n):
        self.result = []
        self.Dfs(n * 2, [], 0, 0)
        return self.result

    def Dfs(self, n, stack, lcount, rcount):
        if n <= 0:
            if lcount - rcount == 0:
                self.result.append("".join(stack))
            return
        stack.append("(")
        self.Dfs(n-1, stack, lcount+1, rcount)
        stack.pop()
        if lcount - rcount > 0:
            stack.append(")")
            self.Dfs(n-1, stack, lcount, rcount+1)
            stack.pop()
        return


obj = Solution()
res = obj.generateParenthesis(n)
print(res)
