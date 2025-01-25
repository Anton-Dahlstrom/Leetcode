class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        pos = [[nums[i], i] for i in range(len(nums))]
        pos.sort()
        l = 0
        while l < len(nums)-1:
            curval, i = pos[l]
            r = l+1
            indexes = [i]
            while r < len(nums):
                nval, j = pos[r]
                if curval + limit < nval:
                    break
                curval = nval
                indexes.append(j)
                r += 1
            indexes.sort()
            for i in range(len(indexes)):
                nums[indexes[i]] = pos[l+i][0]
            l = r

        return nums


nums = [4, 52, 38, 59, 71, 27, 31, 83, 88, 10]
limit = 14
output = [4, 27, 31, 38, 52, 59, 71, 83, 88, 10]

obj = Solution()
res = obj.lexicographicallySmallestArray(nums, limit)
print(res)
print(output)
print(res == output)
