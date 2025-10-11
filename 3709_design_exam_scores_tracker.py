class ExamTracker:

    def __init__(self):
        self.prefix = []
        self.records = []  # time, score

    def record(self, time: int, score: int) -> None:
        self.records.append((time, score))
        prev = 0
        if self.prefix:
            prev = self.prefix[-1]
        self.prefix.append(score + prev)

    def totalScore(self, startTime: int, endTime: int) -> int:
        l, r = 0, len(self.records)-1
        while l <= r:
            mid = l + ((r-l)//2)
            start = self.records[mid][0]
            if start < startTime:  # invalid
                l = mid+1
            elif start >= startTime:  # valid
                r = mid-1
        left = l
        l, r = 0, len(self.records)-1
        while l <= r:
            mid = l + ((r-l)//2)
            end = self.records[mid][0]
            if end > endTime:  # invalid
                r = mid-1
            elif end <= endTime:  # valid
                l = mid+1
        right = r
        if left > right:
            return 0
        res = self.prefix[r]
        if left > 0:
            res -= self.prefix[left-1]
        return res

# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)©leetcode


obj = ExamTracker()
print(obj.record(1, 98))
print(obj.totalScore(1, 1))
print(obj.record(5, 99))
print(obj.totalScore(1, 3))
print(obj.totalScore(1, 5))
print(obj.totalScore(3, 4))
print(obj.totalScore(2, 5))
