from collections import defaultdict


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        hmap = defaultdict(list)
        for i, char in enumerate(word1):
            hmap[char].append(i)

        arr = []

        def findFirstLargerOrSame(val):
            if arr[0] > val:
                return 0
            if arr[-1] < val:
                return len(arr)

            l = 0
            r = len(arr)-1
            while l < r:
                mid = l + ((r-l)//2)
                if arr[mid] < val:
                    l = mid+1
                else:
                    r = mid-1
            if l < len(arr) - 2 and arr[l] < val:
                l += 1
            return l

        for char in word2:
            if hmap[char]:
                matches = hmap[char]
                if not arr:
                    arr.append(matches[0])
                    continue
                for i in matches[::-1]:
                    change = findFirstLargerOrSame(i)
                    if change == len(arr):
                        arr.append(i)
                    else:
                        arr[change] = i
        same = len(arr)
        return (len(word1) - same) + (len(word2) - same)


word1 = "intention"
word2 = "execution"
output = 8

obj = Solution()
res = obj.minDistance(word1, word2)
print(res)
print(output)
print(res == output)
