class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        if not buildings:
            return []
        # skylines = [[0, 0], [float("inf"), 0]]
        skylines = [[0, 0]]
        # Solution should iterate backwards through the previous ranges
        for building in buildings:
            left, right, height = building
            i = len(skylines)-1
            print(skylines)
            while i >= 0 and right >= left:
                sleft,  sheight = skylines[i]
                # print([left, right, height])
                # print([sleft, sheight])
                if right < sleft:
                    i -= 1
                    continue
                # [4, 7, 2]
                # [[0,5], [3,2], [5,0]]
                # [[0,5], [3,2], [7,0]]
                # [1, 7, 2]
                # [[0,5], [3,2], [7,0]]
                # [[0,5], [1,2], [7,0]]
                if height > sheight:
                    if i < len(skylines)-1:
                        if skylines[i+1][1] == height:
                            if left < sleft:
                                skylines[i+1][0] = sleft
                                i -= 1
                                continue
                            else:
                                skylines[i+1][0] = left
                                break

                    elif right > sleft:
                        # skylines[i][0] = right
                        if i == len(skylines)-1:
                            skylines.append([right, height])
                        skylines.insert(i+1, [sleft, height])
                        right = sleft-1
                        i -= 2
                        break
                    skylines.insert(i+1, [sleft, height])
                    right = sleft-1
                    i -= 2
                i -= 1

        return skylines[:-1]


buildings = [[0, 2, 3], [2, 5, 3]]
output = [[0, 3], [5, 0]]

# buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
# output = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]

# buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3]]
# output = [[1, 3], [3, 0]]

# buildings = [[4, 9, 10], [4, 9, 15], [4, 9, 12], [10, 12, 10], [10, 12, 8]]
# output = [[4, 15], [9, 0], [10, 10], [12, 0]]

# buildings = [[2, 9, 10], [12, 15, 10]]
# output = [[2, 10], [9, 0], [12, 10], [15, 0]]

# buildings = [[1, 38, 219], [2, 19, 228], [2, 64, 106], [3, 80, 65], [3, 84, 8], [4, 12, 8], [4, 25, 14], [4, 46, 225], [4, 67, 187], [5, 36, 118], [5, 48, 211], [5, 55, 97], [6, 42, 92], [6, 56, 188], [7, 37, 42], [7, 49, 78], [7, 84, 163], [8, 44, 212], [9, 42, 125], [9, 85, 200], [9, 100, 74], [10, 13, 58], [11, 30, 179], [12, 32, 215], [12, 33, 161], [12, 61, 198], [13, 38, 48], [13, 65, 222], [14, 22, 1], [15, 70, 222], [16, 19, 196], [16, 24, 142], [16, 25, 176], [16, 57, 114], [18, 45, 1], [19, 79, 149], [20, 33, 53], [21, 29, 41], [23, 77, 43], [24, 41, 75], [
#     24, 94, 20], [27, 63, 2], [31, 69, 58], [31, 88, 123], [31, 88, 146], [33, 61, 27], [35, 62, 190], [35, 81, 116], [37, 97, 81], [38, 78, 99], [39, 51, 125], [39, 98, 144], [40, 95, 4], [45, 89, 229], [47, 49, 10], [47, 99, 152], [48, 67, 69], [48, 72, 1], [49, 73, 204], [49, 77, 117], [50, 61, 174], [50, 76, 147], [52, 64, 4], [52, 89, 84], [54, 70, 201], [57, 76, 47], [58, 61, 215], [58, 98, 57], [61, 95, 190], [66, 71, 34], [66, 99, 53], [67, 74, 9], [68, 97, 175], [70, 88, 131], [74, 77, 155], [74, 99, 145], [76, 88, 26], [82, 87, 40], [83, 84, 132], [88, 99, 99]]
# output = [[1, 219], [2, 228], [19, 225], [45, 229], [
#     89, 190], [95, 175], [97, 152], [99, 74], [100, 0]]

obj = Solution()
res = obj.getSkyline(buildings)
print(res)
print(output)
print(res == output)
