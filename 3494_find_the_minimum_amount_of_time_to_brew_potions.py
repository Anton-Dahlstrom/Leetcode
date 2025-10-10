class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        n, m = len(skill), len(mana)
        prev = [0] * (n + 1)
        for j in range(n):
            prev[j+1] = prev[j] + (skill[j] * mana[0])
        for i in range(1, m):  # potion
            l = prev[0]+1
            r = prev[-1]
            while l <= r:
                failed = False
                cur = [0] * (n+1)
                mid = l + ((r-l)//2)
                cur[0] = mid
                for j in range(n):
                    cur[j+1] = cur[j] + (skill[j] * mana[i])
                    if (j < n-1 and cur[j+1] < prev[j+2]):
                        failed = True
                        break
                if failed:
                    l = mid + 1
                else:
                    r = mid - 1
            cur = [0] * (n + 1)
            cur[0] = l
            for j in range(n):
                cur[j+1] = cur[j] + (skill[j] * mana[i])
            prev = cur
        return prev[-1]


skill = [3, 5, 3, 9]
mana = [1, 10, 7, 3]
output = 293


obj = Solution()
res = obj.minTime(skill, mana)
print(res)
print(output)
print(res == output)
