from collections import defaultdict


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        n = len(word)
        count = defaultdict(int)
        size = 0
        for char in word:
            count[char] += 1
            size = max(count[char], size)

        # how many chars of each count
        arr = [0] * (size+1)
        for key in count:
            arr[count[key]] += 1

        # prepares prefix
        smaller = [0] * (size+2)
        for i in range(size):
            end = min(size+1, i+k+1)
            smaller[i+1] += arr[i]*i
            smaller[end] -= arr[i]*i

        # how many chars we can use when our max is of a given index
        prefix = [0] * (size+1)
        cur = 0
        for i in range(len(prefix)):
            cur += smaller[i]
            prefix[i] = cur

        used = 0
        for i in range(size, -1, -1):
            used = max(used, i*arr[i] + prefix[i])
            arr[i-1] += arr[i]
        return n-used


word = "dabdcbdcdcd"
k = 2
output = 2


obj = Solution()
res = obj.minimumDeletions(word, k)
print(res)
print(output)
print(res == output)
