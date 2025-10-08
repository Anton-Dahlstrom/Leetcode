class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        n, m = len(spells), len(potions)
        potions.sort()
        res = [0]*n
        for i in range(n):
            if spells[i] * potions[-1] < success:
                res[i] = 0
                continue
            l = 0
            r = m-1
            while r >= l:
                mid = l + ((r-l)//2)
                if spells[i] * potions[mid] < success:
                    l = mid + 1
                else:
                    r = mid - 1
            res[i] = m-l
        return res


spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
output = [4, 0, 3]

obj = Solution()
res = obj.successfulPairs(spells, potions, success)
print(res)
print(output)
print(res == output)
