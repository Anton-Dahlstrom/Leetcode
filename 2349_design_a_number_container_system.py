import heapq
from collections import defaultdict


class NumberContainers:

    def __init__(self):
        self.indexes = {}
        self.nums = defaultdict(list)
        self.removed = defaultdict(set)

    def change(self, index: int, number: int) -> None:
        if index in self.indexes:
            if self.indexes[index] == number:
                return
            self.removed[self.indexes[index]].add(index)
        self.indexes[index] = number
        if index in self.removed[number]:
            self.removed[number].remove(index)
        heapq.heappush(self.nums[number], index)

    def find(self, number: int) -> int:
        while self.nums[number] and self.nums[number][0] in self.removed[number]:
            heapq.heappop(self.nums[number])
        if self.nums[number]:
            return self.nums[number][0]
        return - 1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
