class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:

        spaces = [startTime[0]]
        spaceSort = [(startTime[0],0)]
        n = len(startTime)
        for i in range(n-1):
            spaceSize = startTime[i+1] - endTime[i]
            spaces.append(spaceSize)
            spaceSort.append((spaceSize, i+1))
        spaces.append(eventTime - endTime[-1])
        spaceSort.append((eventTime - endTime[-1],n))
        spaceSort.sort(reverse=True)


        def checkFlyingMeeting(meetingSize, i):
            for space in spaceSort:
                if space[1] == i or space[1] == i+1:
                    continue
                if space[0] >= meetingSize:
                    return True
                return False

        res = spaces[0]
        for i in range(1, len(spaces)):
            combinedSpace = spaces[i]+spaces[i-1]
            meetingSize = endTime[i-1] - startTime[i-1]
            if checkFlyingMeeting(meetingSize, i-1):
                combinedSpace += meetingSize
            res = max(res, combinedSpace)

        return res


eventTime = 5
startTime = [1,3]
endTime = [2,5]
output= 2

# eventTime = 10
# startTime = [0,7,9]
# endTime = [1,8,10]
# output= 7

# eventTime = 10
# startTime = [0,3,7,9]
# endTime = [1,4,8,10]
# output= 6

# eventTime = 5
# startTime = [0,1,2,3,4]
# endTime = [1,2,3,4,5]
# output= 0

# eventTime = 41
# startTime = [17,24]
# endTime = [19,25]
# output = 24


obj = Solution()
res = obj.maxFreeTime(eventTime, startTime, endTime)
print(res)
print(output)
print(res == output)