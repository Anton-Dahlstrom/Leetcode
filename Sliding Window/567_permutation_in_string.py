s1 = "ab"
s2 = "eidbaooo"
Output: true


# Turn perm string into hmap. If char not in hmap reset the hmap and start after the char.
# If the char doesn't fit in the hmap go from the beginning of the hmap and add to the hmap count
# when you find a char that belongs. Stop adding when you get to the char that didn't fit.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pass

obj = Solution()
answer = obj.checkInclusion(s1, s2)
print(answer)