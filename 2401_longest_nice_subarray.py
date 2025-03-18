class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        res = 1
        bits = nums[0]
        count = 1
        l, r = 0, 1
        while r < n:
            if not bits or bits & nums[r] == 0:
                bits ^= nums[r]
                r += 1
                count += 1
                res = max(res, count)
            else:
                bits ^= nums[l]
                l += 1
                count -= 1
        return res


nums = [84139415, 693324769, 614626365, 497710833, 615598711, 264, 65552, 50331652, 1, 1048576, 16384,
        544, 270532608, 151813349, 221976871, 678178917, 845710321, 751376227, 331656525, 739558112, 267703680]
output = 8

obj = Solution()
res = obj.longestNiceSubarray(nums)
print(res)
print(output)
print(res == output)
