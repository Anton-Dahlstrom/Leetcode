
class SparseTableMax:

    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.log = [0] * (self.n+1)
        self.buildLog()
        self.table = self.buildSparseTable()

    def buildLog(self):
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i//2]+1

    def buildSparseTable(self):
        k = self.log[self.n] + 1
        table = [[0]*k for _ in range(self.n)]

        for i in range(self.n):
            table[i][0] = self.arr[i]

        for j in range(1, k):
            i = 0
            while i + (1 << j) <= self.n:
                table[i][j] = max(
                    table[i][j - 1], table[i + (1 << (j - 1))][j - 1])
                i += 1

        return table

    def query(self, left, right):
        length = right - left + 1
        j = self.log[length]
        return max(self.table[left][j], self.table[right - (1 << j) + 1][j])


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        MOD = (10**9) + 7
        n = len(nums)
        m = max(nums)+1
        arr = [0] * m
        arr[0] = arr[1] = 1
        # Calculate primes
        for i in range(m//2+1):
            if arr[i]:
                continue
            for nonprime in range(i, m, i):
                arr[nonprime] += 1

        scores = [0] * n
        for i in range(n):
            val = nums[i]
            if val < 2:
                scores[i] = 0
            elif not arr[val]:
                scores[i] = 1
            else:
                scores[i] = arr[val]

        table = SparseTableMax(scores)
        nums = [(nums[i], i) for i in range(n)]
        nums.sort()
        res = 1
        while nums:
            val, i = nums.pop()
            score = scores[i]
            l = r = i

            if i > 0:
                if table.query(0, i-1) < score:
                    l = 0
                elif scores[i-1] >= score:
                    l = i
                else:
                    templ = 0
                    tempr = i-1
                    while templ < tempr:
                        mid = templ + ((tempr-templ)//2)
                        # we know there is a >= element, we need to find it
                        # if mid-tempr is safe, we know the element is in an index less than mid so we move tempr left of mid
                        if table.query(mid, tempr) < score:
                            tempr = mid-1
                        else:
                            templ = mid
                        l = templ+1
            if i < n-1:
                if table.query(i+1, n-1) <= score:
                    r = n-1
                elif scores[i+1] > score:
                    r = i
                else:
                    templ = i+1
                    tempr = n-1
                    while templ < tempr:
                        mid = templ + ((tempr-templ)//2)
                        if table.query(templ, mid) <= score:
                            templ = mid+1
                        else:
                            tempr = mid
                    r = templ-1
            leftsize = i-l+1
            rightsize = r-i+1
            totalsize = leftsize * rightsize
            res *= val ** min(totalsize, k)
            res %= MOD
            k -= totalsize
            if k <= 0:
                break
        return res


nums = [8, 3, 9, 3, 8]
k = 2
output = 81

# nums = [19, 12, 14, 6, 10, 18]
# k = 3
# output = 4788


# nums = [8, 3, 9, 3, 8]
# k = 2
# output = 81

nums = [3289, 2832, 14858, 22011]
k = 6
output = 256720975

obj = Solution()
res = obj.maximumScore(nums, k)
print(res)
print(output)
print(res == output)
