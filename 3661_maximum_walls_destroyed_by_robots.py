from typing import List


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # pos, dist
        n = len(robots)
        robots = [(robots[i], distance[i]) for i in range(len(robots))]
        robots.sort()
        walls.sort()
        right = walls.copy()
        left = walls
        rres = 0
        lres = 0
        while robots and (left or right):
            pos, dist = robots.pop()
            nextrobot = 0
            if robots:
                nextrobot = robots[-1][0]
            # remove robots out of range
            while right and right[-1] > pos+dist:
                right.pop()
            while left and left[-1] > pos+dist:
                left.pop()

            # get best result when shooting right
            rsize = len(right) - 1
            lsize = len(left) - 1
            r = rsize
            l = lsize
            lr = lsize
            while r >= 0 and right[r] >= pos:
                r -= 1
            while l >= 0 and left[l] >= pos and left[l] > nextrobot:
                l -= 1
            while lr >= 0 and left[lr] >= pos and left[lr] > nextrobot:
                lr -= 1
            temprres = max(lres + lsize-l, rres + rsize-r, lres + lsize-lr)
            # remove the robots we shot
            while right and right[-1] > pos:
                right.pop()
            while left and left[-1] > pos:
                left.pop()

            # get best result when shooting left
            rsize = len(right) - 1
            lsize = len(left) - 1
            r = rsize
            l = lsize
            while r >= 0 and right[r] >= pos-dist and right[r] > nextrobot:
                r -= 1
            while l >= 0 and left[l] >= pos-dist and left[l] > nextrobot:
                l -= 1
            lres = max(lres + lsize-l, rres + rsize-r)
            rres = temprres
            # remove the robots we shot
            while left and left[-1] >= pos-dist and left[-1] > nextrobot:
                left.pop()
            if right and right[-1] == pos:
                right.pop()

        return max(rres, lres)
