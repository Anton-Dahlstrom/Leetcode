# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order

from typing import List
nums = [1, 2, 3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# An inefficient brute-force approach would be to generate every combination and try to add the sorted combination as a key to a hashmap.
# That way you weed out any duplicates and are only left with unique permutations without repetition.

# Maybe there is an approach that could remove an increasing amount of elements per loop-cycle?
# First it removes none, then it removes each number once, then it removes each combination of two numbers etc. and saves the results.


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []


obj = Solution()
obj.subsets(nums)
