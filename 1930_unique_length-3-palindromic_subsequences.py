from typing import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = Counter(s)
        left = {}
        found = set()
        for char in s:
            right[char] -= 1
            if not right[char]:
                right.pop(char)
                if char in left:
                    left.pop(char)

            for lchar in left:
                found.add(lchar+char+lchar)

            if char in right:
                left[char] = 1

        return len(found)


s = "bbcbaba"
output = 4

obj = Solution()
res = obj.countPalindromicSubsequence(s)
print(res)
print(output)
print(res == output)
