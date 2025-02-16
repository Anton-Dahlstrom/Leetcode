class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        arr = [0] * (n * 2 - 1)
        added = set()

        def dfs(i):
            if i == len(arr):
                return True
            if arr[i]:
                if dfs(i+1):
                    return True
                else:
                    return False
            for num in range(n, 0, -1):
                if num in added:
                    continue
                if num != 1:
                    if i+num >= len(arr):
                        return False
                    if arr[i+num]:
                        continue

                arr[i] = num
                if num != 1:
                    arr[i+num] = num
                added.add(num)
                if dfs(i+1):
                    return True
                arr[i] = 0
                if num != 1:
                    arr[i+num] = 0
                added.remove(num)
            return False
        dfs(0)
        return arr


n = 3
output = [3, 1, 2, 3, 2]

n = 5
output = [5, 3, 1, 4, 3, 5, 2, 4, 2]

n = 2
output = [2, 1, 2]

obj = Solution()
res = obj.constructDistancedSequence(n)
print(res)
print(output)
print(res == output)
