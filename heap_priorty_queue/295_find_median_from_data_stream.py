class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        if not self.nums or num > self.nums[-1]:
            self.nums.append(num)
            return
        l = 0
        r = len(self.nums)
        while l <= r:
            mid = l + ((r-l)//2)
            if num == self.nums[mid]:
                self.nums.insert(mid, num)
                return
            elif num < self.nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        if num > self.nums[mid]:
            self.nums.insert(max(mid+1, 0), num)
            return
        self.nums.insert(mid, num)

    def findMedian(self):
        length = len(self.nums)
        if length % 2:
            return self.nums[length//2]
        return (self.nums[length//2] + self.nums[length//2-1])/2


arr = [[6], [], [10], [], [2], [], [6], [], [5], [], [
    0], [], [6], [], [3], [], [1], [], [0], [], [0], []]
output = [6, 8.0, 6, 6.0, 6, 5.5, 6, 5.5, 5, 4.0, 3]

obj = MedianFinder()
res = []
for val in arr:
    if not val:
        res.append(obj.findMedian())
    else:
        obj.addNum(val[0])
print(res)
print(res == output)
