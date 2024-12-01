class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        nums = set()
        for n in arr:
            if n * 2 in nums:
                return True
            if not n % 2 and n//2 in nums:
                return True
            nums.add(n)
        return False

arr = [10,2,5,3]
output = True

obj = Solution()
res = obj.checkIfExist(arr)
print(res)
print(output)
print(res == output)
        