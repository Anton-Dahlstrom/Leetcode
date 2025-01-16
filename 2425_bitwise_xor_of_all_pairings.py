class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        num1found = 0
        num2found = 0
        n1xor = 0
        n2xor = 0
        for n1 in nums1:
            num1found |= n1
            n1xor ^= n1

        for n2 in nums2:
            num2found |= n2
            n2xor ^= n2

        res = 0
        largest = max(num1found, num2found)
        i = 0
        while True:
            val = 1 << i
            if val > largest:
                break
            if val & num1found == val and val & n1xor == val:
                if (len(nums2) - ((n2xor & val) >> i)) % 2 == 1:
                    res ^= val
            if val & num2found == val and val & n2xor == val:
                if (len(nums1) - ((n1xor & val) >> i)) % 2 == 1:
                    res ^= val
            i += 1
        return res


nums1 = [2, 1, 3]
nums2 = [10, 2, 5, 0]
output = 13

obj = Solution()
res = obj.xorAllNums(nums1, nums2)
print(res)
print(output)
print(res == output)
