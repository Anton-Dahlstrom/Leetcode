class NumArray:

    def __init__(self, nums: list[int]):
        self.arr = nums.copy()
        for i in range(1, len(self.arr)):
            self.arr[i] += self.arr[i-1]

    def sumRange(self, left: int, right: int) -> int:
        res = self.arr[right]
        if left > 0:
            res -= self.arr[left-1]

        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
