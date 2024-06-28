from typing import List


class TrieNode():
    def __init__(self):
        self.nodes = {}
        self.last = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return None
        res = []
        found = set()

        def makeTries(strings: list):
            if not strings:
                return None
            root = TrieNode()
            for string in strings:
                cur = root
                for char in string:
                    if char not in cur.nodes:
                        cur.nodes[char] = TrieNode()
                    cur = cur.nodes[char]
                cur.last = True
            return root

        def gridSearch(y: int, x: int, grid: list[list[str]], chars: dict[str]) -> list[int]:
            matches = []
            if y > 0:
                if grid[y-1][x] in chars:
                    matches.append([y-1, x])
            if y < len(grid)-1:
                if grid[y+1][x] in chars:
                    matches.append([y+1, x])
            if x > 0:
                if grid[y][x-1] in chars:
                    matches.append([y, x-1])
            if x < len(grid[0])-1:
                if grid[y][x+1] in chars:
                    matches.append([y, x+1])
            return matches

        def dfs(coords, grid, trie, string, visited):
            y, x = coords
            coords = tuple(coords)
            if coords in visited:
                return
            visited.add(coords)
            char = grid[y][x]
            string += char
            node = trie.nodes[char]
            if node.last:
                if string not in found:
                    res.append(string)
                    found.add(string)
            matches = gridSearch(y, x, grid, node.nodes)
            for match in matches:
                dfs(match, grid, node, string, visited)
            visited.remove(coords)

        trie = makeTries(words)
        for y in range(0, len(board)):
            for x in range(0, len(board[0])):
                if board[y][x] in trie.nodes:
                    dfs([y, x], board, trie, "", set())
        return res


board = [["o", "a", "a", "n"],
         ["e", "t", "a", "e"],
         ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
output = ["eat", "oath"]

# board = [["a"]]
# words = ["a"]
# output = ["a"]

# board = [["o", "a", "b", "n"], ["o", "t", "a", "e"], [
#     "a", "h", "k", "r"], ["a", "f", "l", "v"]]
# words = ["oa", "oaa"]
# output = ["oa", "oaa"]

# board = [["a", "a"]]
# words = ["a"]
# output = ["a"]

# board = [["a", "a"]]
# words = ["aaa"]
# output = []

board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
         ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain", "hklf", "hf"]
output = ["oath", "eat", "hklf", "hf"]

obj = Solution()
res = obj.findWords(board, words)
print(res)
