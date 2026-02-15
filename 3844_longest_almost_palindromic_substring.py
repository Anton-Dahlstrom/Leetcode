class Solution:
    def almostPalindromic(self, s: str) -> int:
        def findPalindrome(s: str, l: int, r: int, first: bool):
            res = 0
            while l >= 0 and r <= len(s)-1:
                if s[l] != s[r]:
                    if first:
                        if l > 0:
                            res = max(res, findPalindrome(s, l-1, r, False))
                        if r < len(s)-1:
                            res = max(res, findPalindrome(s, l, r+1, False))
                    break
                l -= 1
                r += 1
            # this is the size after we pull l and r back together so they form a valid palindrome
            size = r-l-1
            if first:
                size += 1
            res = max(res, size)
            return res
        n = len(s)
        res = 0
        for i in range(n):
            res = max(res, findPalindrome(s, i, i, True))
            res = max(res, findPalindrome(s, i, i+1, True))

        return min(n, max(2, res))
