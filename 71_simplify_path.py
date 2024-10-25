class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return

        dirs = path.split("/")
        if not dirs[-1]:
            dirs.pop()
        i = 0
        while i < len(dirs):
            if dirs[i] == ".":
                dirs.pop(i)
            elif dirs[i] == "..":
                dirs.pop(i)
                if i > 0:
                    dirs.pop(i-1)
                    i-=1
            elif not dirs[i]:
                dirs.pop(i)
            else:
                i += 1

        res ="/" + "/".join(dirs)
        if not res:
            res = "/"
        return res

path = "/home/user//Documents/../Pictures/" 
output = "/home/user/Pictures"

path = "/../"
output = "/"

# path = "/a/./b/../../c/"
# output = "/c"

path = "/home/../../.."
output = "/"

obj = Solution()
res = obj.simplifyPath(path)
print(res)
print(output)
print(res == output)