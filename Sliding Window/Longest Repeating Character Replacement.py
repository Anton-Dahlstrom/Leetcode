# s = "ABAB" 
# k = 2
# 4 

# s = "AABABBA" 
# k = 1
# 4

# s = "BAAA"
# k = 0
# answer: 3

s = "aBBB"
k = 2
4
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        r = 0
        hmap = {}
        current = 0
        while r < len(s):
            char = s[r]
            current += 1
            if char not in hmap:
                hmap[char] = 1
            else:
                hmap[char] += 1
            if current - hmap[max(hmap, key=hmap.get)] > k:
                while l < r and current - hmap[max(hmap, key=hmap.get)] > k:
                    reduce = s[l]
                    hmap[reduce] -= 1
                    current -= 1
                    l += 1
            r += 1
            longest = max(current, longest)
        return longest

obj = Solution()
answer = obj.characterReplacement(s, k)
print(answer)
