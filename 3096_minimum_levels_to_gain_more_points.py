class Solution:
    def minimumLevels(self, possible: list[int]) -> int:
        n = len(possible)
        for i in range(n):
            if not possible[i]:
                possible[i] = -1
            if i:
                possible[i] += possible[i-1]
        for i in range(n-1):
            if possible[i] > possible[-1] - possible[i]:
                return i+1
        return -1


possible = [1, 1, 1, 1, 1]
output = 3

possible = [1, 0, 1, 0]
output = 1

obj = Solution()
res = obj.minimumLevels(possible)
print(res)
print(output)
print(res == output)
