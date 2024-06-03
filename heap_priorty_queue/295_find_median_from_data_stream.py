import math
class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        self.heap.append(num)
        i = len(self.heap)-1
        while i > 0:
            parent = (i - 1)//2 
            if self.heap[parent] < self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[parent]
                self.heap[parent] = temp
            i = parent
        print(self.heap)
#            0
#     1,             2
# 3,     4,      5,      6
#7, 8, 9, 10, 11, 12, 13, 14
# 4-7 == 3
#
# 1, 3, 7, 15

    def findMedian(self) -> float:
        odd = len(self.heap) % 2
        cuts = math.log2((len(self.heap) //2))
        sets = [(self.heap[0], 0)]
        count = 0
        while count < cuts:
            count += 1
            i = 0
            for i in range(len(sets)):
                if sets[i][1] < len(self.heap) //2:
                    break
            set = sets[i]
            i = set[1]
            l = i*2 + 1
            if l < len(self.heap):
                l = (self.heap[l], l)
                j = 0
                while l[0] > self.heap[j] and j < len(self.heap):
                    j += 1
                sets.insert(j, l)
            r = i*2 + 2
            if r < len(self.heap):
                r = (self.heap[r], r)
                j = 0
                while r[0] > self.heap[j] and j < len(self.heap):
                    j += 1
                sets.insert(j, r)
        print(sets)
        if odd:
            return float(sets[0][0])
        return (sets[0][0] + sets[1][0]) / 2

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
# obj.addNum(2)
obj.addNum(4)
obj.addNum(5)
# obj.addNum(7)

res = obj.findMedian()
print(res)