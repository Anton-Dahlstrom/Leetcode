class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        arr = [0]*value
        while nums:
            num = nums.pop()
            arr[num % value] += 1
        i = 0
        while i < 10**5:
            rem = i % value
            if not arr[rem]:
                return i
            arr[rem] -= 1
            i += 1
        return i


nums = [1, -10, 7, 13, 6, 8]
value = 5
output = 4

obj = Solution()
res = obj.findSmallestInteger(nums, value)
print(res)
print(output)
print(res == output)
