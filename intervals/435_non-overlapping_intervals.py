from typing import List

intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
output = 1

intervals = [[-25322, -4602], [-35630, -28832], [-33802, 29009], [13393, 24550], [-10655, 16361], [-2835, 10053], [-2290, 17156], [1236, 14847], [-45022, -1296], [-34574, -1993], [-14129, 15626], [3010, 14502],
             [42403, 45946], [-22117, 13380], [7337, 33635], [-38153, 27794], [47640, 49108], [40578, 46264], [-38497, -13790], [-7530, 4977], [-29009, 43543], [-49069, 32526], [21409, 43622], [-28569, 16493], [-28301, 34058]]
output = 19
# intervals.sort()
# print(intervals)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def checkOverlap(interval1, interval2):
            if interval1[0] >= interval2[1] or interval2[0] >= interval1[1]:
                return False
            if interval1[1] <= interval2[0] or interval2[1] <= interval1[0]:
                return False
            return True
        count = 0
        hmap = {}
        for interval in intervals:
            interval = tuple(interval)
            if interval in hmap:
                count += 1
                continue
            temp = [0, set()]
            for item in hmap:
                if checkOverlap(interval, item):
                    temp[0] += 1
                    temp[1].add(item)
                    hmap[item][0] += 1
                    hmap[item][1].add(interval)
            hmap[interval] = temp

        key = max(hmap, key=hmap.get)
        while hmap[key][0] > 0:
            # if count == 16:
            #     break
            count += 1
            val = hmap.pop(key)
            for interval in val[1]:
                hmap[interval][0] -= 1
                hmap[interval][1].remove(key)
            key = max(hmap, key=hmap.get)
        for key in hmap:
            print(key)
            print(hmap[key])
            print("----------")
        return count


obj = Solution()
res = obj.eraseOverlapIntervals(intervals)
print(res)
print(res == output)
