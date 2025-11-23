class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> list[int]:
        sum = int((n/2)*(n+1))
        if sum < abs(target):
            return []
        if (sum - abs(target)) % 2:
            return []
        neg = (sum-target)//2
        used = set()
        res = []
        while neg:
            num = min(neg, n)
            if num == n:
                n -= 1
            res.append(-num)
            used.add(num)
            neg -= num

        for i in range(1, n+1):
            if i not in used:
                res.append(i)
        return res


n = 3
target = 0
output = [-3, 1, 2]

obj = Solution()
res = obj.lexSmallestNegatedPerm(n, target)
print(res)
print(output)
print(res == output)
