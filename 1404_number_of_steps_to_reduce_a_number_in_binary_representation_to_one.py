class Solution:
    def numSteps(self, s: str) -> int:
        arr = list(s)
        res = 0
        while arr[-1] == "0":
            arr.pop()
            res += 1
        n = len(arr)
        if n > 1:
            res += 1
        for i in range(n-1, 0, -1):
            if arr[i] == "1":
                res += 1
                for j in range(i-1, 0, -1):
                    if arr[j] == "1":
                        arr[j] = "0"
                    else:
                        arr[j] = "1"
                        break
            res += 1
        return res
