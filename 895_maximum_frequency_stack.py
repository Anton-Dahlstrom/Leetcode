import heapq


class FreqStack:

    def __init__(self):
        self.freq = {}
        # freq[val], i, val
        self.heap = []
        self.i = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        heapq.heappush(self.heap, (-self.freq[val], -self.i, val))
        self.i += 1

    def pop(self) -> int:
        cnt, time, val = heapq.heappop(self.heap)
        self.freq[val] -= 1
        return val

        # Your FreqStack object will be instantiated and called as such:
        # obj = FreqStack()
        # obj.push(val)
        # param_2 = obj.pop()
