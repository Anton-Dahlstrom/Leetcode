class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = 0
        open = 0
        for c in s:
            if c == "[":
                open += 1
                pass
            else:
                if open:
                    open -= 1
                else:
                    swaps += 1
        return swaps//2 + swaps % 2


s = "]]][[["
output = 2

obj = Solution()
res = obj.minSwaps(s)
print(res)
print(output)
print(res == output)
