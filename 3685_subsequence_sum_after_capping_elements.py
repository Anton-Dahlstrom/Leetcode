class Solution:
    def subsequenceSumAfterCapping(self, nums: list[int], k: int) -> list[bool]:
        nums.sort()
        n = len(nums)
        res = []
        arr = [False]*(k+1)  # we never have to look beyond index k
        arr[0] = True
        p = 0
        for cap in range(1, n+1):
            valid = False
            for j in range(k, -1, -1):  # search arr
                if arr[j]:
                    if (not (k - j) % cap and ((n-p)*cap) + j >= k) or arr[k]:
                        valid = True
            while p < n and nums[p] <= cap:
                val = nums[p]
                for j in range(k, -1, -1):
                    if arr[j]:
                        if (not (k - j) % cap and ((n-p)*cap) + j >= k) or arr[k]:
                            valid = True
                        if j+val <= k:
                            arr[j+val] = True
                p += 1
                if val <= k:
                    arr[val] = True
            if arr[k]:
                break
            res.append(valid)
        return res + [True]*(n-len(res))


nums = [4, 3, 2, 4]
k = 5
output = [False, False, True, True]


obj = Solution()
res = obj.subsequenceSumAfterCapping(nums, k)
print(res)
print(output)
print(res == output)
