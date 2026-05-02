class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid = {3, 4, 7}
        unchanged = {0, 1, 8}
        changed = {2, 5, 6, 9}
        res = 0
        for i in range(1, n+1):
            good = False
            cur = i
            while cur:
                digit = cur % 10
                cur //= 10
                if digit in unchanged:
                    continue
                elif digit in changed:
                    good = True
                elif digit in invalid:
                    good = False
                    break
            if good:
                res += 1
        return res
