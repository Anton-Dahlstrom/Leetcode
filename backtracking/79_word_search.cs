// solution exceeds timelimit, should run dfs right away when looking for coords.

public class Solution
{
    Dictionary<int, Dictionary<int, int>> visited = [];
    public bool Exist(char[][] board, string word)
    {
        for (int i = 0; i < board.Length; i++)
        {
            visited.Add(i, []);
            for (int j = 0; j < board[i].Length; j++)
            {
                if (board[i][j] == word[0])
                {
                    visited[i].Add(j, 1);
                    visited[i][j] = 1;
                    bool result = Dfs(board, word, i, j, 1);
                    visited[i].Remove(j);
                    if (result)
                    {
                        return true;
                    }
                }
            }
            visited = [];
        }
        return false;
    }

    // Need to make sure the GridSearch function doesn't try to visit a previous node.
    // Maybe by having a hashmap with each previously written letter as the key and a list
    // of coordinates as values, when a match is found it checks if the coordinates are
    // identical to any of the coordinate values in the hashmap and if so skips that coordinate.
    public IList<IList<int>> GridSearch(char[][] board, char target,
             int y, int x)
    {
        IList<IList<int>> res = [];
        for (int j = x - 1; j < Math.Min(x + 2, board[y].Length); j += 2)
        {
            if (j < 0)
            {
                continue;
            }
            else if (board[y][j] == target)
            {
                res.Add([y, j]);
            }
        }
        for (int i = y - 1; i < Math.Min(board.Length, y + 2); i += 2)
        {
            if (i < 0)
            {
                continue;
            }
            else if (board[i][x] == target)
            {
                res.Add([i, x]);
            }
        }
        foreach (IList<int> r in res)
        {
            Console.WriteLine(string.Join(" ", r));
        }
        return res;
    }

    public bool Dfs(char[][] board, string word,
             int y, int x, int index)
    {
        Console.WriteLine("dfs");
        if (index >= word.Length)
        {
            return true;
        }
        Console.WriteLine($"{y}, {x}");
        IList<IList<int>> coords = GridSearch(board, word[index], y, x);
        foreach (IList<int> coord in coords)
        {
            if (visited.TryGetValue(coord[0], out Dictionary<int, int> visitedY))
            {
                if (visitedY != null && visitedY.TryGetValue(coord[1], out int val))
                {
                    continue;
                }
                else
                {
                    visitedY.Add(coord[1], 1);
                }
            }
            else
            {
                visited.Add(coord[0], []);
                visited[coord[0]].Add(coord[1], 1);
            }
            bool res = Dfs(board, word, coord[0], coord[1], index + 1);
            visited[coord[0]].Remove(coord[1]);
            if (res)
            {
                Console.WriteLine("returning here");
                Console.WriteLine(index);
                Console.WriteLine($"{y} {x}");
                return true;
            }
        }
        return false;
    }
}
