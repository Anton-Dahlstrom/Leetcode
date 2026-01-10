class Solution:
    def totalScore(self, hp: int, damage: list[int], requirement: list[int]) -> int:
        n = len(damage)
        res = 0
        damageTaken = [0]*(n+1)
        cur = 0
        for i in range(n-1, -1, -1):
            cur += damage[i]
            damageTaken[i] = cur

        def bs(arr, val, l=0, r=None):
            if r == None:
                r = len(arr)-1
            while l <= r:
                mid = l + ((r-l)//2)
                if arr[mid] > val:
                    l = mid+1
                else:
                    r = mid-1
            return r

        for i in range(n-1, -1, -1):
            canTank = hp - requirement[i]
            canTank += damageTaken[i+1]
            firstRoom = bs(damageTaken, canTank, 0, i)
            res += i-firstRoom
        return res


hp = 11
damage = [3, 6, 7]
requirement = [4, 2, 5]
output = 3


obj = Solution()
res = obj.totalScore(hp, damage, requirement)
print(res)
print(output)
print(res == output)
