class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False

        n = len(s)
        arr = [0]*n
        arr[0] = 1
        l = -1

        for i in range(n):
            if arr[i]:
                left = max(l, i+minJump)
                right = min(n, i+maxJump+1)
                for j in range(left, right):
                    if s[j] == "0":
                        arr[j] = 1
                l = right

        return arr[-1] == 1
