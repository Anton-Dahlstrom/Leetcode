from functools import partial
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def binarySearch(self, arr, target):
        if not arr or target < arr[0][0]:
            return ""
        l = 0
        r = len(arr)-1
        mid = 0
        while l <= r:
            mid = l + ((r-l)//2)
            if target == arr[mid][0]:
                return arr[mid][1]
            elif target > arr[mid][0]:
                l = mid + 1
            else:
                r = mid - 1
        if target < arr[mid][0]:
            if mid == len(arr) - 1:
                return ""
            else:
                mid -= 1
        return arr[mid][1]

    def binaryInsert(self, arr: list, val):
        if not arr:
            arr.append(val)
            return
        l = 0
        r = len(arr)-1
        mid = 0
        while l <= r:
            mid = l + ((r-l)//2)
            if val == arr[mid]:
                arr.insert(mid, val)
                return
            elif val > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        if val > arr[mid]:
            if mid == len(arr) - 1:
                arr.append(val)
            else:
                arr.insert(mid+1, val)
        else:
            arr.insert(mid, val)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.binaryInsert(self.hmap[key], [timestamp, value])

        # for k, v in self.hmap.items():
        #     print(k, v)

    def get(self, key: str, timestamp: int) -> str:
        return self.binarySearch(self.hmap[key], timestamp)


def test(obj, vals):
    print(vals)
    operation = vals[0]
    args = vals[1]
    if operation == "set":
        res = obj.set(*args)
    elif operation == "get":
        res = obj.get(*args)
    print(res)


# operations = ["set", "get", "get", "set", "get", "get"]
# argArray = [["foo", "bar", 1], ["foo", 1], ["foo", 3],
#             ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

operations = ["set", "set", "get", "get", "get", "get", "get"]
argArray = [["love", "high", 10], ["love", "low", 20], ["love", 5],
            ["love", 10], ["love", 15], ["love", 20], ["love", 25]]

zipped = list(zip(operations, argArray))
obj = TimeMap()
part = partial(test, obj)
list(map(part, zipped))

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key, value, timestamp)
# param_2 = obj.get(key, timestamp)
