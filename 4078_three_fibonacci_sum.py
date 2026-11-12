class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        arr = [0,1,1]
        cur = -1
        while cur <= n:
            cur = sum(arr)
            if cur == n:
                return True
            arr[0], arr[1], arr[2] = arr[1], arr[2], arr[1] + arr[2]
        return False