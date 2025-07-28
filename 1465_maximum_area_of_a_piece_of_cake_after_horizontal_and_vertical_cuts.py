class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        MOD = 10**9 + 7
        horizontal, vertical = 0, 0
        prevCut = 0
        for cut in verticalCuts + [w]:
            horizontal = max(horizontal, cut-prevCut)
            prevCut = cut
        prevCut = 0
        for cut in horizontalCuts + [h]:
            vertical = max(vertical, cut-prevCut)
            prevCut = cut
        return horizontal * vertical % MOD


h = 5
w = 4
horizontalCuts = [3, 1]
verticalCuts = [1]
output = 6

obj = Solution()
res = obj.maxArea(h, w, horizontalCuts, verticalCuts)
print(res)
print(output)
print(res == output)
