s1 = "ab"
s2 = "eidbaooo"
Output: True

Input: s1 = "ab"
s2 = "eidboaoo"
Output: False

s1 = "abc"
s2 ="cccccbabbbaaaa"
True

# Turn perm string into hmap. If char not in hmap reset the hmap and start after the char.
# If the char doesn't fit in the hmap go from the beginning of the hmap and add to the hmap count
# when you find a char that belongs. Stop adding when you get to the char that didn't fit.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        for char in s1:
           hmap[char] = 1 + hmap.get(char, 0)
        temp = hmap.copy()
        l = 0
        for r, char in enumerate(s2):
            if char not in hmap:
                if max(temp.values()) < 1:
                    return True
                temp = hmap.copy()
                l = r+1
            else:
                temp[char] -= 1
                if max(temp.values()) < 1:
                    return True
                if temp[char] < 0:
                    for removingChar in s2[l:]: 
                        print(l, r)
                        print(removingChar)
                        if removingChar in temp:
                            temp[removingChar] += 1
                        l += 1
                        if removingChar == char:
                            print(temp)
                            print("breaking")
                            break
        if max(temp.values()) < 1:
            return True
        else: 
            return False

obj = Solution()
answer = obj.checkInclusion(s1, s2)
print(answer)