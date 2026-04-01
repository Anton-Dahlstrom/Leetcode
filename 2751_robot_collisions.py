from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        # position, health, index
        left = []
        right = []
        for i in range(n):
            if directions[i] == "L":
                left.append([positions[i], healths[i], i])
            else:
                right.append([positions[i], healths[i], i])
        left.sort(reverse=True)
        right.sort()
        res = []

        def bs(arr, val):
            l, r = 0, len(arr)-1
            while l <= r:
                mid = l + ((r-l)//2)
                if arr[mid][0] >= val:
                    r = mid-1
                else:
                    l = mid+1
            return l-1
        while left:
            if not right:
                res += [(robot[2], robot[1]) for robot in left]
                break
            lpos, lhp, li = left.pop()
            while right:
                j = bs(right, lpos)
                if j < 0:
                    break
                rpos, rhp, ri = right[j]
                if lhp > rhp:
                    lhp -= 1
                    right.pop(j)
                    if not lhp:
                        break
                elif lhp < rhp:
                    right[j][1] -= 1
                    lhp = 0
                    if not right[j][1]:
                        right.pop(j)
                    break
                elif lhp == rhp:
                    right.pop(j)
                    lhp = 0
                    break
            if lhp:
                res.append((li, lhp))

        right = [(robot[2], robot[1]) for robot in right]
        res += right
        res.sort()
        res = [hp for i, hp in res]
        return res
