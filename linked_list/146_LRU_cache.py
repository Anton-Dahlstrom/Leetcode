text = ["LRUCache", "put", "put", "get",
        "put", "get", "put", "get", "get", "get"]
nums = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

class LinkNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = 0
        self.hmap = {}
        self.array = []

    def get(self, key: int) -> int:
        if key in self.hmap:
            moving = self.array.pop(self.hmap[key][1])
            moving[1] = len(self.array) - 1
            self.array.append(moving)
            return self.hmap[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.hmap[key] = [value, len(self.array)-1]
            moving = self.array.pop(self.hmap[key][1])
            moving[1] = len(self.array) - 1
            self.array.append(moving)
        else:
            if self.keys < self.capacity:
                self.keys += 1
                self.hmap[key] = [value, self.keys-1]
                self.array.append(key)
            else:
                self.hmap.pop(self.array.pop(0))
                self.array.append(key)
                self.hmap[key] = [value, self.capacity-1]


lRUCache = LRUCache(nums[0])

for i in range(1, len(text)):

