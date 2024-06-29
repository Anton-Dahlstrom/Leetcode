from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Finds the querys matching interval.
        def binarySearchInterval(intervals: list[list[int], int], val: int):
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

        # Helps us create a sorted array of intervals based on original size.
        def uniteIntervals(inter1, inter2):
            # print(inter1, inter2, "HERE")
            # Size of inter1 is always greater.
            if inter1[1] < inter2[1]:
                inter1, inter2 = inter2, inter1
            inter1, size1 = inter1
            inter2, size2 = inter2
            l1, r1 = inter1
            l2, r2 = inter2
            res = []
            # The conditionals check if anything should be added before or after inter2.
            if l2 > l1:
                res.append([[l1, l2-1], size1])
            res.append([[l2, r2], size2])
            if r1 > r2:
                res.append([[r2+1, r1], size1])
            return res

        # Creates a list of non-overlapping intervals with the size of the smallest interval.
        intervals.sort(key=lambda i: i[0])
        arr = []
        for interval in intervals[0:]:
            size = interval[1] - interval[0] + 1
            arr.append([interval, size])
            i = len(arr) - 1
            while i > 0 and len(arr) > 1:
                j = i - 1
                # If the interval we're inserting is smaller than the right-most interval
                # we continue searching for smaller intervals it might overlap with.
                while arr[i][0][1] < arr[j][0][0] and j >= 0:
                    j -= 1
                # If the interval is too large we break since continuing will only bring
                # smaller intervals.
                if arr[i][0][0] > arr[i-1][0][1]:
                    break
                cur = arr.pop(i)
                prev = arr.pop(j)
                # If intervals don't overlap we break.
                order = uniteIntervals(prev, cur)
                arr[j:j] = order
                i = j
        res = []
        for query in queries:
            res.append(binarySearchInterval(arr, query))
        return res


intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]
output = [3, 3, 1, 4]

intervals = [[9, 9], [1, 10], [1, 3], [9, 10], [
    8, 8], [1, 5], [3, 8], [5, 5], [1, 6], [1, 9]]
queries = [8, 1, 5, 1, 5, 7, 1, 9, 8, 1]
output = [1, 3, 1, 3, 1, 6, 3, 1, 1, 3]

intervals = [[54, 82], [55, 66], [81, 89], [38, 67], [81, 86], [47, 47], [13, 61], [33, 39], [61, 66], [97, 97], [52, 68], [96, 98], [89, 92], [1, 41], [81, 89], [9, 57], [81, 90], [41, 73], [29, 80], [98, 98], [61, 95], [93, 98], [5, 65], [91, 96], [91, 99], [28, 68], [55, 71], [35, 45], [1, 89], [48, 48], [26, 36], [5, 83], [20, 83], [73, 92], [69, 69], [77, 89], [12, 52], [5, 53], [33, 53], [70, 83], [81, 98], [69, 69], [28, 90], [9, 77], [40, 53], [53, 71], [7, 55], [7, 28], [5, 88], [61, 68], [
    25, 93], [45, 73], [13, 51], [27, 70], [47, 87], [71, 91], [93, 98], [1, 35], [24, 39], [86, 90], [19, 33], [1, 69], [21, 100], [85, 85], [99, 99], [25, 25], [90, 94], [13, 61], [69, 85], [89, 97], [1, 43], [11, 35], [41, 95], [31, 99], [86, 94], [33, 63], [22, 91], [61, 75], [71, 83], [31, 85], [28, 83], [1, 21], [81, 97], [5, 29], [74, 83], [33, 83], [13, 24], [92, 94], [71, 71], [59, 79], [21, 37], [33, 87], [97, 97], [34, 57], [11, 59], [57, 62], [22, 23], [13, 53], [84, 85], [71, 80]]
queries = [31, 9, 21, 91, 91, 58, 13, 76, 21, 69, 41, 1, 73, 2, 71, 51, 69, 89, 31, 85, 61, 61, 39, 76, 36, 50, 1, 33, 41, 38, 29, 91, 93, 47, 1, 11, 33, 79, 15, 7, 21, 36, 65, 1, 1, 93, 45, 51, 33,
           5, 15, 65, 49, 81, 59, 21, 1, 7, 81, 6, 1, 80, 81, 21, 24, 41, 47, 85, 38, 26, 100, 33, 57, 24, 71, 16, 65, 96, 81, 83, 17, 75, 76, 21, 85, 47, 77, 49, 31, 61, 9, 49, 1, 73, 32, 66, 96, 97, 30, 21]
output = [11, 21, 12, 4, 4, 6, 12, 10, 12, 1, 11, 21, 10, 21, 1, 14, 1, 4, 11, 1, 6, 6, 7, 10, 7, 14, 21, 7, 11, 7, 11, 4, 3, 1, 21, 21, 7, 10, 12, 21, 12, 7, 6, 21, 21, 3, 11, 14, 7,
          21, 12, 6, 14, 6, 6, 12, 21, 21, 6, 21, 21, 10, 6, 12, 12, 11, 1, 1, 7, 11, 80, 7, 6, 12, 1, 12, 6, 3, 6, 6, 12, 10, 10, 12, 1, 1, 10, 14, 11, 6, 21, 14, 21, 10, 11, 6, 3, 1, 11, 12]
obj = Solution()
res = obj.minInterval(intervals, queries)
print(res)
print(res == output)
