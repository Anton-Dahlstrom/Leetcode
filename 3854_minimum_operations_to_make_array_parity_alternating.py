from typing import List


class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0, 0]
        n = len(nums)
        minmax = [min(nums), max(nums)]
        evenmoves = 0
        eventemp = nums.copy()
        for i in range(n):
            if i % 2 == 0 and nums[i] % 2 == 1:
                if nums[i] < minmax[1]:
                    eventemp[i] += 1
                else:
                    eventemp[i] -= 1
                evenmoves += 1
            if i % 2 == 1 and nums[i] % 2 == 0:
                if nums[i] < minmax[1]:
                    eventemp[i] += 1
                else:
                    eventemp[i] -= 1
                evenmoves += 1

        oddmoves = 0
        oddtemp = nums.copy()
        for i in range(n):
            if i % 2 == 0 and nums[i] % 2 == 0:
                if nums[i] < minmax[1]:
                    oddtemp[i] += 1
                else:
                    oddtemp[i] -= 1
                oddmoves += 1
            if i % 2 == 1 and nums[i] % 2 == 1:
                if nums[i] < minmax[1]:
                    oddtemp[i] += 1
                else:
                    oddtemp[i] -= 1
                oddmoves += 1
        moves = min(oddmoves, evenmoves)
        diff = minmax[1] - minmax[0]

        if evenmoves == moves:
            diff = min(diff, max(eventemp)-min(eventemp))
            eventemp = nums.copy()
            for i in range(n):
                if i % 2 == 0 and nums[i] % 2 == 1:
                    if nums[i] > minmax[0]:
                        eventemp[i] -= 1
                    else:
                        eventemp[i] += 1
                if i % 2 == 1 and nums[i] % 2 == 0:
                    if nums[i] > minmax[0]:
                        eventemp[i] -= 1
                    else:
                        eventemp[i] += 1
            diff = min(diff, max(eventemp)-min(eventemp))

        if oddmoves == moves:
            diff = min(diff, max(oddtemp)-min(oddtemp))
            oddtemp = nums.copy()
            for i in range(n):
                if i % 2 == 0 and nums[i] % 2 == 0:
                    if nums[i] > minmax[0]:
                        oddtemp[i] -= 1
                    else:
                        oddtemp[i] += 1
                if i % 2 == 1 and nums[i] % 2 == 1:
                    if nums[i] > minmax[0]:
                        oddtemp[i] -= 1
                    else:
                        oddtemp[i] += 1
            diff = min(diff, max(oddtemp)-min(oddtemp))
        diff = max(1, diff)
        return [moves, diff]
