class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        cnt = 0
        for i in range(len(arr)):
            if arr[i] % 2:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False


arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
output: True

obj = Solution()
res = obj.threeConsecutiveOdds(arr)
print(res)
print(output)
print(res == output)
