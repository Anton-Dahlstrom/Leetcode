from collections import defaultdict


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        hmap = defaultdict(int)
        for char in s:
            hmap[char] += 1

        best = 0
        mostFreq = 0
        counts = defaultdict(list)
        for char in hmap:  # char
            charCount = hmap[char]
            counts[charCount].append(char)
            size = len(counts[charCount])
            if size == best and charCount > mostFreq:
                best = size
                mostFreq = charCount
            elif size > best:
                best = size
                mostFreq = charCount

        return "".join(counts[mostFreq])


s = "aaabbbccdddde"
output = "ab"

obj = Solution()
res = obj.majorityFrequencyGroup(s)
print(res)
print(output)
print(res == output)
