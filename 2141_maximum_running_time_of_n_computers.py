class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:

        batteries.sort()
        unused = sum(batteries[:-n])
        nums = batteries[-n:]
        res = nums[0]
        i = 0
        left = nums[i]
        while i < n-1:
            while i < n-2 and left == nums[i+1]:
                i += 1
            right = nums[i+1]
            size = i+1
            spaceToAdd = (right-left)*size
            if unused >= spaceToAdd:
                unused -= spaceToAdd
                res += spaceToAdd//size
                left += spaceToAdd//size
            else:
                break
            i += 1
        res += unused//min((i+1), n)
        return res


n = 3
batteries = [10, 10, 6, 9, 3]
output = 12

obj = Solution()
res = obj.maxRunTime(n, batteries)
print(res)
print(output)
print(res == output)
