class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        cnt = 0
        for i in range(n-1, -1, -1):
            if s[i] not in vowels:
                break
            cnt += 1
        return s[:n-cnt]
