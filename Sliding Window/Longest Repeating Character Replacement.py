# s = "ABAB" 
# k = 2
#4 

# s = "AABABBA" 
# k = 1
# 4

# s = "BAAA"
# k = 0
# answer: 3

# s = "aBBB"
# k = 2
# 4
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        i = 0
        while i < len(s):
            hmap = {}
            substring = ""
            current = 0
            r = i
            i += 1
            while r < len(s):
                char = s[r]
                substring += char
                if char not in hmap:
                    hmap[char] = 1
                else:
                    hmap[char] += 1
                
                if len(substring) - hmap[max(hmap, key=hmap.get)] > k:
                    print(hmap, k)
                    print(substring, hmap[max(hmap, key=hmap.get)])
                    longest = max(longest, current)
                    break
                r += 1
                current += 1
                longest = max(current, longest)
        return longest

obj = Solution()
answer = obj.characterReplacement(s, k)
print(answer)

# asd = {"a": [2, 5], "d": [3, 500]}
# asd2 = max(asd, key=asd.get)
# print(asd2)