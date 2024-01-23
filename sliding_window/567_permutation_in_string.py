s1 = "ab"
s2 = "eidbaooo"
Output: True


# Turn perm string into hmap. If char not in hmap reset the hmap and start after the char.
# If the char doesn't fit in the hmap go from the beginning of the hmap and add to the hmap count
# when you find a char that belongs. Stop adding when you get to the char that didn't fit.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        for char in s1:
           hmap[char] = 1 + hmap.get(char, 0)
        print(hmap)
        temp = hmap.copy()
        start = 0
        for i, char in enumerate(s2):
            if char not in hmap:
                temp = hmap.copy()
                start = 0
            else:
                if not start:
                    start = i
                hmap[char] -= 1
                if hmap[char] < 0:
                    pass

        temp[55] = 1
        print(hmap)

obj = Solution()
answer = obj.checkInclusion(s1, s2)
print(answer)