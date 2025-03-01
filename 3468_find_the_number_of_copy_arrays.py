class Solution:
    def countArrays(self, original: list[int], bounds: list[list[int]]) -> int:
        n = len(original)
        diffs = [0]
        for i in range(1, n):
            diffs.append(original[i] - original[i-1])
        bot, top = bounds[0]

        for i in range(1, n):
            bot = max(bot+diffs[i], bounds[i][0])
            top = min(top+diffs[i], bounds[i][1])
            if bot > top:
                return 0

        return top-bot+1


original = [1, 2, 3, 4]
bounds = [[1, 2], [2, 3], [3, 4], [4, 5]]
output = 2

original = [1, 2, 3, 4]
bounds = [[1, 10], [2, 9], [3, 8], [4, 7]]
output = 4

original = [1, 2, 1, 2]
bounds = [[1, 1], [2, 3], [3, 3], [2, 3]]
output = 0

obj = Solution()
res = obj.countArrays(original, bounds)
print(res)
print(output)
print(res == output)
