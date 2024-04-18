from typing import List

k = 3
nums = [4, 5, 8, 2]
input = [3, 5, 10, 9, 4]
output = [4, 5, 5, 8, 8]

k = 1
nums = []
input = [-3, -2, -4, 0, 4]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        temp = [float('-inf')] * k
        if not nums:
            self.array = temp
            return
        for i in range(0, len(nums)):
            for j in range(0, len(temp)):
                if nums[i] < temp[j]:
                    break
            if k:
                if nums[i] > temp[-1]:
                    temp.append(nums[i])
                else:
                    temp.insert(j, nums[i])
                k -= 1
            else:
                if j:
                    temp.insert(j, nums[i])
                    temp.pop(0)
        self.array = temp
        return None

    def add(self, val: int) -> int:
        for i in range(0, len(self.array)):
            if val < self.array[i]:
                break
        if i:
            if val > self.array[-1]:
                self.array.append(val)
            else:
                self.array.insert(i, val)
            self.array.pop(0)
        else:
            if val > self.array[0]:
                self.array[0] = val
        if len(self.array) >= self.k:
            index = self.k * -1
            if self.array[index] == float('-inf'):
                return None
            return self.array[index]
        return None


obj = KthLargest(k, nums)
result = []
for num in input:
    res = obj.add(num)
    result.append(res)

print(result)
print(result == output)
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

a = float('-inf')
print(type(a))
print(a > 5)
