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
        n = len(nums)
        m = max(nums)+1
        arr = [True] * m
        arr[0] = arr[1] = False
        primes = []
        for i, isprime, in enumerate(arr):
            if isprime:
                primes.append(i)
                for nonprime in range(i*i, m, i):
                    arr[nonprime] = False

        scores = [0]*n
        for i in range(n):
            val = nums[i]
            if arr[val]:
                scores[i] = 1
                continue
            score = 0
            for prime in primes:
                if val % prime:
                    continue
                score += 1
                while not val % prime:
                    val = val//prime
                    if val == 1:
                        break
            scores[i] = score

        table = SparseTableMax(nums)

        # we split subarrays based on the biggest score in the subarray
        # the value with the biggest score gets the size of the subarray as amount he can use from K
        # use sparse table to find the biggest number for a given subarray, then we find it's index

        return


nums = [8, 3, 9, 3, 8]
k = 2
output = 81

obj = Solution()
res = obj.maximumScore(nums, k)
print(res)
print(output)
print(res == output)
