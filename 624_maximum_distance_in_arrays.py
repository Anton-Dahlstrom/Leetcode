
class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        if arrays[0][0] < arrays[1][0]:
            s1 = arrays[0][0]
            s2 = arrays[1][0]
            si = 0
        else:
            s1 = arrays[1][0]
            s2 = arrays[0][0]
            si = 1

        if arrays[0][-1] > arrays[1][-1]:
            l1 = arrays[0][-1]
            l2 = arrays[1][-1]
            li = 0
        else:
            l1 = arrays[1][-1]
            l2 = arrays[0][-1]
            li = 1

        for i in range(2, len(arrays)):
            arr = arrays[i]
            if arr[0] < s1:
                s2 = s1
                s1 = arr[0]
                si = i
            elif arr[0] < s2:
                s2 = arr[0]

            if arr[-1] > l1:
                l2 = l1
                l1 = arr[-1]
                li = i
            elif arr[-1] > l2:
                l2 = arr[-1]
        if li != si:
            return l1 - s1
        else:
            return max(l1 - s2, l2 - s1)


arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
output = 4


obj = Solution()
res = obj.maxDistance(arrays)
print(res)
print(output)
print(res == output)
