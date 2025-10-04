class Solution:
    def minSplitMerge(self, nums1: list[int], nums2: list[int]) -> int:
        if nums1 == nums2:
            return 0
        n = len(nums1)
        target = tuple(nums2)
        states = set()
        depth = 1
        arrs = [nums1]
        while arrs:
            temp = []
            for arr in arrs:
                for i in range(n):
                    for j in range(i+1, n+1):
                        cut = arr[i:j]
                        left = arr[:i]
                        right = arr[j:]
                        merged = left+right
                        for k in range(len(merged)+1):
                            combined = merged[:k] + cut + merged[k:]
                            state = tuple(combined)
                            if state == target:
                                return depth
                            if state in states:
                                continue
                            states.add(state)
                            temp.append(combined.copy())
            arrs = temp
            depth += 1
        return 1


nums1 = [3, 1, 2]
nums2 = [1, 2, 3]
output = 1

nums1 = [1, 1, 2, 3, 4, 5]
nums2 = [5, 4, 3, 2, 1, 1]
output = 3

obj = Solution()
res = obj.minSplitMerge(nums1, nums2)
print(res)
print(output)
print(res == output)
