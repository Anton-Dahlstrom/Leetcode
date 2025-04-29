class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        bot, top, cur = 0, 0, 0
        for diff in differences:
            cur += diff
            bot = min(cur, bot)
            top = max(cur, top)
        res = upper-lower+1
        res -= top-bot
        return max(0, res)


differences = [3, -4, 5, 1, -2]
lower = -4
upper = 5
output = 4

obj = Solution()
res = obj.numberOfArrays(differences, lower, upper)
print(res)
print(output)
print(res == output)
