class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        n = len(pushed)
        i, j = 0, 0
        stack = []
        while i < n or j < n:
            if i < n and (not stack or stack[-1] != popped[j]):
                stack.append(pushed[i])
                i += 1
            elif stack[-1] == popped[j]:
                j += 1
                stack.pop()
            else:
                return False
        return True


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
output = True

obj = Solution()
res = obj.validateStackSequences(pushed, popped)
print(res)
print(output)
print(res == output)
