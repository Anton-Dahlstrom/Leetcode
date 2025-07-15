class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        n = len(people)
        res = 0
        l, r = 0, n-1
        while l <= r:
            if people[r] > limit:
                r -= 1
                continue
            res += 1
            if people[r] + people[l] <= limit:
                l += 1
            r -= 1
        return res


people = [2, 49, 10, 7, 11, 41, 47, 2, 22,
          6, 13, 12, 33, 18, 10, 26, 2, 6, 50, 10]
limit = 50
output = 11

obj = Solution()
res = obj.numRescueBoats(people, limit)
print(res)
print(output)
print(res == output)
