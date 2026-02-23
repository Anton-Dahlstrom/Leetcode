class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        found = set()
        for i in range(n-k+1):
            found.add(s[i:i+k])
        return len(found) == 2**k
