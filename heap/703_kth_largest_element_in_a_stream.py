from typing import List

k = 3
nums = [4, 5, 8, 2]
input = [3, 5, 10, 9, 4]
output = [4, 5, 5, 8, 8]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass


obj = KthLargest(k, nums)
result = []
for num in input:
    res = obj.add(num)
    result.append(res)
print(result == output)
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
