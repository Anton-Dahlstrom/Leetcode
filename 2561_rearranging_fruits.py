from collections import defaultdict


class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        n = len(basket1)
        diff = defaultdict(int)
        for i in range(n):
            diff[basket1[i]] += 1
            diff[basket2[i]] -= 1
        arr1 = []
        arr2 = []

        for key in diff:
            if diff[key] % 2:
                return -1
            if diff[key] > 0:
                arr1.append([key, diff[key]])
            elif diff[key] < 0:
                arr2.append([key, diff[key]*-1])
        minimum = min(min(basket1), min(basket2))
        arr1.sort()
        arr2.sort()
        l1, r1, l2, r2 = 0, len(arr1)-1, 0, len(arr2)-1
        res = 0
        while l1 <= r1 and l2 <= r2:
            if arr1[l1][0] < arr2[l2][0]:
                res += min(minimum*2, arr1[l1][0])
                arr1[l1][1] -= 2
                if not arr1[l1][1]:
                    l1 += 1

                arr2[r2][1] -= 2
                if not arr2[r2][1]:
                    r2 -= 1

            else:
                res += min(minimum*2, arr2[l2][0])
                arr2[l2][1] -= 2
                if not arr2[l2][1]:
                    l2 += 1

                arr1[r1][1] -= 2
                if not arr1[r1][1]:
                    r1 -= 1
        if l1 <= r1 or l2 <= r2:
            return -1
        return res


basket1 = [4, 2, 2, 2]
basket2 = [1, 4, 1, 2]
output = 1


obj = Solution()
res = obj.minCost(basket1, basket2)
print(res)
print(output)
print(res == output)
