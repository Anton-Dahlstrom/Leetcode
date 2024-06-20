num1 = [1,3,6,8,9,24,32]
num2 = [4,6,7,8,22,32,45,56,57]
num1 = []
num2 = []

num1 = [3]
num2 = [-2,-1]
output = -1

num1 = [1,3]
num2 = [2]
output = 2

num1 = [1,2]
num2 = [-1,3]
output = 1.5

class Solution():

    def findMedianSortedArrays(self, num1, num2):
        if not num1 and not num2:
            return None
        totalNums = len(num1) + len(num2)
        even = True
        if totalNums % 2:
            even = False
        if not num1:
            if even:
                return (num2[len(num2)//2] + num2[len(num2)//2 - 1]) / 2
            else:
                return num2[len(num2)//2]
        if not num2:
            if even:
                return (num1[len(num1)//2] + num1[len(num1)//2 - 1]) / 2
            else:
                return num1[len(num1)//2]
        
        removeTop = totalNums // 2
        removeBot = totalNums // 2
        if even:
            removeTop -= 1
            removeBot -= 1
        l1 = 0
        l2 = 0
        r1 = len(num1) - 1
        r2 = len(num2) - 1
        res1, res2 = 0,0
        while removeBot > 0 and removeTop > 0:
            mid1 = l1 + ((r1 - l1)//2)       
            mid2 = l2 + ((r2 - l2)//2)
            print("pointers: ", l1, r1, l2, r2)
            print("mids: ", mid1, mid2)
            print("remove: ", removeTop, removeBot) 
            if l1 == r1:
                res1 = l1
                if not even:
                    return num1[l1]
            if l2 == r2:
                res2 = l2
                if not even:
                    return num2[l2]

            if removeTop > removeBot:
                if num1[mid1] > num2[mid2]:
                    if removeTop - (r1 - (r1 - mid1) - 1) >= 0:
                        removeTop -= (r1 -(r1 - mid1) - 1)
                        r1 = mid1 -1
                        if r1 < 0:
                            removeTop -= r1
                            r1 = 0
                    else:
                        r1 -= removeTop
                        removeTop = 0

                else:
                    if removeTop - (r2 - (r2 - mid2)) + 1 >= 0:
                        removeTop -= (r2 -(r2 - mid2)) + 1
                        r2 = mid2 -1
                    else:
                        r2 -= removeTop
                        removeTop = 0

            else:
                if num1[mid1] < num2[mid2]:
                    if removeBot - (mid1 - l1 + 1) >= 0:
                        removeBot -= (mid1 - l1 + 1)
                        l1 = mid1 + 1
                    else:
                        l1 += removeBot
                        removeBot = 0
                else:
                    if removeBot - (mid2 - l2 + 1) >= 0:
                        removeBot -= (mid2 - l2 + 1)
                        l2 = mid2 + 1
                    else:
                        l2 += removeBot
                        removeBot = 0

        if not even:
            if res1:
                return num1[res1]
            else:
                return num2[res2]
        if not res1:
            res1 = l1
        if not res2:
            res2 = l2
        print("pointers: ", l1, r1, l2, r2)
        print("mids: ", mid1, mid2)
        print("remove: ", removeTop, removeBot) 
        print(res1, res2)
        return (num1[res1] + num2[res2])/2
    

print(num1, num2)
obj = Solution()
res = obj.findMedianSortedArrays(num1, num2)
print(res)

# output = num1 + num2
# print(len(output))
# output.sort()
# print(output[7], output[8])