class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        ages.sort()
        arr = []
        prev = float("inf")
        for age in ages:
            if age == prev:
                arr[-1][1] += 1
            else:
                arr.append([age, 1])
                prev = age
        n = len(arr)
        res = 0
        for i in range(n):
            if arr[i][0] > (0.5 * arr[i][0] + 7):
                res += arr[i][1] * (arr[i][1]-1)
            for j in range(i+1, n):
                if arr[i][0] <= 0.5 * arr[j][0] + 7:
                    break
                res += arr[i][1] * arr[j][1]
        return res


ages = [101, 56, 69, 48, 30]
output = 4


obj = Solution()
res = obj.numFriendRequests(ages)
print(res)
print(output)
print(res == output)
