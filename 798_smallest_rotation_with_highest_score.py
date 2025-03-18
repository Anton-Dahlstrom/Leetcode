class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        n = len(nums)
        starts = []
        stops = []
        for i in range(n):
            val = nums[i]
            if not val:
                continue
            start = (i+1) % n
            if start:
                starts.append(start)
            stop = (i+n-val+1)
            if stop > n:
                starts.append(0)
                stops.append(stop % n)
            else:
                stops.append(stop)

        starts.sort()
        stops.sort()
        maxpoint = 0
        res = 0
        cur = 0
        starti = 0
        stopi = 0
        for i in range(n):
            while starti < len(starts) and starts[starti] == i:
                cur += 1
                starti += 1
            while stopi < len(stops) and stops[stopi] == i:
                cur -= 1
                stopi += 1
            if cur > maxpoint:
                maxpoint = cur
                res = i
        return res

        # calculate allowed positions
        # turn it into ranges allowed
        # [0,2,3,1]
        # rotation on index 1 gives
        # [2,3,1,0]
        # <= their index gives points
        # what rotation indexes are allowed for each num
        # arr = [0,2,3,1]
        # ans = [[0,1,2,3], [2,3], [3], [1,2,3]]
        #
        # nums = [2,3,1,4,0]
        # [1, 2, 3] for 2 on index 0
        # [2, 3] for 3 on index 1
        # [0, 1, 3, 4] for 1 on index 2
        # [4] for 4 on index 3
        # [0,1,2,3,4] for 0 on index 4
        #
        # pattern:
        # you can always rotate i+1 to i + n-val


nums = [2, 3, 1, 4, 0]
output = 3

nums = [1, 3, 0, 2, 4]
output = 0


obj = Solution()
res = obj.bestRotation(nums)
print(res)
print(output)
print(res == output)
