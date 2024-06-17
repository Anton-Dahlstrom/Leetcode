text = ["LRUCache", "put", "put", "get",
        "put", "get", "put", "get", "get", "get"]
nums = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output = [null, null, null, 1, null, -1, null, -1, 3, 4]


class LinkNode:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LinkList:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.root = LinkNode()
        self.tail = LinkNode()
        self.root.next = self.tail
        self.tail.prev = self.root

    def insertHead(self, node: LinkNode):
        node.next = self.root.next
        self.root.next = node
        node.next.prev = node
        node.prev = self.root

    def popNode(self, node: LinkNode):
        prev = node.prev
        next = node.next
        prev.next = next
        if next:
            next.prev = prev
        else:
            self.cutTail()
        node.prev = None
        node.next = None
        return node

    def cutTail(self):
        if self.tail.val == None:
            self.tail = self.tail.prev
        oldTail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return oldTail


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        self.linklist = LinkList(capacity)
        self.hmap = {}

    def get(self, key: int) -> int:
        if key in self.hmap:
            if self.capacity == 1:
                return self.hmap[key].val
            node = self.hmap[key]
            self.linklist.popNode(node)
            self.linklist.insertHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 1:
            if key in self.hmap:
                self.hmap[key].val = value
            else:
                self.hmap = {key: LinkNode(key, value)}
            return

        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            self.linklist.popNode(node)
            self.linklist.insertHead(node)
        else:
            if self.used < self.capacity:
                self.used += 1
            else:
                tail = self.linklist.cutTail()
                self.hmap.pop(tail.key)
            node = LinkNode(key, value)
            self.linklist.insertHead(node)
            self.hmap[key] = node


cache = LRUCache(nums[0][0])
for i in range(1, len(nums)):
    if text[i] == "get":
        print(cache.get(nums[i][0]))
    elif text[i] == "put":
        cache.put(nums[i][0], nums[i][1])
