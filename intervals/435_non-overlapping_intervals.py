from typing import List

intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
output = 1

intervals = [[-25322, -4602], [-35630, -28832], [-33802, 29009], [13393, 24550], [-10655, 16361], [-2835, 10053], [-2290, 17156], [1236, 14847], [-45022, -1296], [-34574, -1993], [-14129, 15626], [3010, 14502],
             [42403, 45946], [-22117, 13380], [7337, 33635], [-38153, 27794], [47640, 49108], [40578, 46264], [-38497, -13790], [-7530, 4977], [-29009, 43543], [-49069, 32526], [21409, 43622], [-28569, 16493], [-28301, 34058]]
output = 19


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0
        for start, end in intervals[1:]:
            print(start, end, prevEnd)
            if start < prevEnd:
                count += 1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end
        return count


obj = Solution()
res = obj.eraseOverlapIntervals(intervals)
print(res)
print(res == output)
