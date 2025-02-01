class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        spaces = [startTime[0]]
        n = len(startTime)

        for i in range(n-1):
            spaces.append(startTime[i+1] - endTime[i])
        spaces.append(eventTime - endTime[-1])
        prefix = [0]*len(spaces)

        res = 0
        
        for i in range(len(spaces)):
            prefix[i] += spaces[i]
            if i > 0:
                prefix[i] += prefix[i-1]
        

        for i in range(len(prefix)):
            if i > k:
                best = prefix[i] - prefix[i-k-1]
                res = max(res, best)
            else:
                res = max(res, prefix[i])
        return res


eventTime = 5
k = 1
startTime = [1,3]
endTime = [2,5]
output= 2

eventTime = 10
k = 1
startTime = [0,2,9]
endTime = [1,4,10]
output= 6

eventTime = 5
k = 2
startTime = [0,1,2,3,4]
endTime = [1,2,3,4,5]
output= 0

eventTime = 99
k = 1
startTime = [7,21,25]
endTime = [13,25,78]
output = 21

obj = Solution()
res = obj.maxFreeTime(eventTime, k, startTime, endTime)
print(res)
print(output)
print(res == output)
