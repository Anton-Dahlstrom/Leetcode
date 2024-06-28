from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        def binarySearchInterval(intervals: list[list[int], int], val: int):
            l = 0
            r = len(intervals) - 1
            print(r)
            print(intervals)
            while l < r:
                print(l, r)
                mid = (l + (r-l))//2
                low, high = intervals[mid][0]
                if val in range(low, high+1):
                    return intervals[mid][1]
                elif val < low:
                    r = mid - 1
                else:
                    l = mid + 1
            print(l, r)
            return -1

        # Creates a list of non-overlapping intervals with the size of the smallest interval.
        intervals.sort(key=lambda i: i[0])
        arr = [[intervals[0], intervals[0][1] - intervals[0][0] + 1]]
        for cur in intervals[1:]:
            print(arr)
            size = cur[1] - cur[0] + 1
            i = len(arr)-1
            while i >= 0:
                l, r = cur
                arr[i]
                prevSize = arr[i][1]
                if l > arr[i][0][1]:
                    break
                if size < prevSize:
                    # Need to never overstep next interval in the array's left value.
                    arr[i][0][1] = l-1
                    if arr[i][0][1] < arr[i][0][0]:
                        arr.pop(i)
                        i -= 1
                    arr.append([[l, r], size])
                    if arr[i][0][1] > r:
                        temp = [[r+1, arr[i][0][1]], arr[i][1]]
                        arr.append(temp)

                elif r >= arr[i][0][1]:
                    arr.append([[arr[i][0][1]+1, r], size])
                i -= 1
        print(arr)

        # res = []
        # for query in queries:
        #     res.append(binarySearchInterval(arr, query))
        # print(res)


intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]
output = [3, 3, 1, 4]
obj = Solution()
res = obj.minInterval(intervals, queries)
print(res)
print(res == output)
