class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        right = {}
        left = {}
        n = len(nums)
        res = [0]*n
        for i in range(n):
            num = nums[i]
            if num not in right:
                right[num] = [i, 1]
            else:
                right[num][0] += i
                right[num][1] += 1
        for i in range(n):
            num = nums[i]
            rsum = rcount = 0
            if num in right:
                right[num][0] -= i
                right[num][1] -= 1
                rsum, rcount = right[num]
                diff = rsum - i*rcount
                res[i] += diff

            if num not in left:
                left[num] = [i, 1]
            else:
                lsum, lcount = left[num]
                diff = i*lcount - lsum
                res[i] += diff
                left[num][0] += i
                left[num][1] += 1
        return res


nums = [5, 0, 10, 5, 5, 1, 0, 5]
output = [14, 5, 0, 8, 8, 0, 5, 14]

obj = Solution()
res = obj.distance(nums)
print(res)
print(output)
print(res == output)
