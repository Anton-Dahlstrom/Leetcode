matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 3
Output: True

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13
# Output: False

# matrix = [[1]]
# target = 1
# Output: True

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        array = []
        while l <= r:
            mid = l + (r - l // 2)
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                array = matrix[mid]
                break
        print(array)
        if array:
            l = 0
            r = len(array) - 1
            while l <= r:
                mid = l + (r - l // 2)
                if target < array[mid]:
                    r = mid - 1
                elif target > array[mid]:
                    l = mid + 1
                elif target == array[mid]:
                    return True
        return False
    
obj = Solution()
answer = obj.searchMatrix(matrix, target)
print(answer)