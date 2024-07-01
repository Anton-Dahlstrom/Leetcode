from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        if not intervals:
            return

        def binarySearchIntervalSize(intervals: list[list[int], int], val: int):
            l = 0
            r = len(intervals) - 1
            while l <= r:
                mid = l + ((r-l)//2)
                low, high = intervals[mid][0]
                if val in range(low, high+1):
                    return intervals[mid][1]
                elif val < low:
                    r = mid - 1
                elif val > high:
                    l = mid + 1
            return -1

        def binarySearchIntervalIndex(intervals: list[list[int], int], val: int):
            l = 0
            r = len(intervals) - 1
            while l <= r:
                mid = l + ((r-l)//2)
                low, high = intervals[mid][0]
                if val in range(low, high+1):
                    return mid
                elif val < low:
                    r = mid - 1
                elif val > high:
                    l = mid + 1
            return None

        intervals.sort(key=lambda i: -(i[1] - i[0] + 1))
        res = []
        arr = [[intervals[0], intervals[0][1] - intervals[0][0] + 1]]

        for interval in intervals:
            size = interval[1] - interval[0] + 1
            lowest, highest = arr[0][0][0], arr[-1][0][1]
            curL, curR = interval[0], interval[1]
            if curL > highest:
                if curL - highest > 1:
                    arr.append([[highest+1, curL-1], -1])
                arr.append([[curL, curR], size])
            elif curR < lowest:
                if lowest - curR > 1:
                    arr.insert(0, [[curR+1, lowest-1], -1])
                arr.insert(0, [[curL, curR], size])
            else:
                leftIndex = None
                rightIndex = None
                if curL >= lowest:
                    leftIndex = binarySearchIntervalIndex(arr, curL)
                if curR <= highest:
                    rightIndex = binarySearchIntervalIndex(arr, curR)

                new = []
                leftArr = []
                if leftIndex is not None:
                    if arr[leftIndex][0][0] < curL:
                        leftArr = [[arr[leftIndex][0][0], curL-1],
                                   arr[leftIndex][1]]
                else:
                    leftIndex = 0
                if leftArr:
                    new.append(leftArr)

                new.append([[curL, curR], size])
                rightArr = []
                if rightIndex is not None:
                    if arr[rightIndex][0][1] > curR:
                        rightArr = [
                            [curR + 1, arr[rightIndex][0][1]], arr[rightIndex][1]]
                else:
                    rightIndex = len(arr)-1
                if rightArr:
                    new.append(rightArr)
                arr[leftIndex:rightIndex+1] = new

        for query in queries:
            res.append(binarySearchIntervalSize(arr, query))
        return res


intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]
queries = [2, 19, 5, 22]
output = [2, -1, 4, 6]


obj = Solution()
res = obj.minInterval(intervals, queries)
print(res)
print(res == output)
