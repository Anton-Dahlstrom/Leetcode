class Solution:
    def maxPoints(self, technique1: list[int], technique2: list[int], k: int) -> int:
        n = len(technique1)
        arr = []
        res = 0
        # Find all the differences and compute sum before swapping techniques
        for i in range(n):
            res += max(technique1[i], technique2[i])
            diff = technique1[i] - technique2[i]
            arr.append(diff)
        arr.sort(reverse=True)

        # Greedyily swap the techniques with the smallest difference
        for i in range(k):
            if arr[i] < 0:
                res += arr[i]
        return res


technique1 = [5, 2, 10]
technique2 = [10, 3, 8]
k = 2

output = 22

obj = Solution()
res = obj.maxPoints(technique1, technique2, k)
print(res)
print(output)
print(res == output)
