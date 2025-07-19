class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort(key=lambda x: x.count("/"))
        roots = set()
        for f in folder:
            root = True
            for i in range(1, len(f)):
                if f[i] == '/' and f[:i] in roots:
                    root = False
                    break
            if root:
                roots.add(f)
        return list(roots)


folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
output = ["/a", "/c/d", "/c/f"]

obj = Solution()
res = obj.removeSubfolders(folder)
print(res)
print(output)
print(res == output)
