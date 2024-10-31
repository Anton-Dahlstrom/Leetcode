class Solution:
    def sortColors(self, nums: list[int]) -> None:

        def quickSort(arr, start, pivot):
            startPivot = pivot
            i = start
            while i < pivot:
                if arr[i] > arr[pivot]:
                    if pivot - i > 1:
                        arr[pivot], arr[pivot-1] = arr[pivot-1], arr[pivot]
                    arr[i], arr[pivot] = arr[pivot], arr[i]
                    pivot -= 1
                else:
                    i += 1
            if (pivot - start) > 1:
                quickSort(arr, start, pivot-1)
            if (startPivot - pivot) > 1:
                quickSort(arr, pivot+1, startPivot)

        quickSort(nums, 0, len(nums)-1)


nums = [2, 0, 2, 1, 1, 0]
output = [0, 0, 1, 1, 2, 2]

nums = [1, 0]
output = [0, 1]


obj = Solution()
res = obj.sortColors(nums)
print(nums)
print(output)
print(nums == output)
