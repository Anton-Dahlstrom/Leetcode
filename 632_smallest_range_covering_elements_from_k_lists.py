import heapq


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        # keep heapq of value and indexes of the array
        # keep track of maxval when entering into the heapq
        # pop smallest val, look at next one (new smallest) and maxval to calculate if we update res

        heap = []  # value, index of array, index inside array
        maxval = -float("inf")
        for k in range(len(nums)):
            heapq.heappush(heap, (nums[k][0], k, 0))
            maxval = max(nums[k][0], maxval)
        res = [heap[0][0], maxval]

        while True:
            val, arri, i = heapq.heappop(heap)
            if i >= len(nums[arri])-1:
                return res
            else:
                val = nums[arri][i+1]
                heapq.heappush(heap, (val, arri, i+1))
                maxval = max(maxval, val)
            minval = heap[0][0]
            if (maxval - minval) < (res[1] - res[0]):
                res[0], res[1] = minval, maxval


nums = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8], [-9, 9], [-10, 10], [-11, 11], [-12, 12], [-13, 13], [-14, 14], [-15, 15], [-16, 16], [-17, 17], [-18, 18], [-19, 19], [-20, 20], [-21, 21], [-22, 22], [-23, 23], [-24, 24], [-25, 25], [-26, 26], [-27, 27], [-28, 28],
        [-29, 29], [-30, 30], [-31, 31], [-32, 32], [-33, 33], [-34, 34], [-35, 35], [-36, 36], [-37, 37], [-38, 38], [-39, 39], [-40, 40], [-41, 41], [-42, 42], [-43, 43], [-44, 44], [-45, 45], [-46, 46], [-47, 47], [-48, 48], [-49, 49], [-50, 50], [-51, 51], [-52, 52], [-53, 53], [-54, 54], [-55, 55]]
output = [-55, -1]

obj = Solution()
res = obj.smallestRange(nums)
print(res)
print(output)
print(res == output)
