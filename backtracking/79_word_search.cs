public class Solution
{
    Dictionary<char, IList<IList<int>>> visited = [];
    public bool Exist(char[][] board, string word)
    {
        visited.Add(word[0], []);
        for (int i = 0; i < board.Length; i++)
        {
            for (int j = 0; j < board[i].Length; j++)
            {
                if (board[i][j] == word[0])
                {
                    visited[word[0]].Add([i, j]);
                    bool result = Dfs(board, word, i, j, 1);
                    visited[word[0]] = [];
                    if (result)
                    {
                        return true;
                    }
                }
            }
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
        int remove;
        bool found;
        if (index >= word.Length)
        {
            return true;
        }
        Console.WriteLine($"{y}, {x}");
        IList<IList<int>> coords = GridSearch(board, word[index], y, x);
        foreach (IList<int> coord in coords)
        {
            remove = 0;
            found = false;
            if (visited.TryGetValue(word[index], out IList<IList<int>>? charvisits))
            {
                for (int i = visited[word[index]].Count - 1; i >= 0; i--)
                {
                    if (visited[word[index]][i] == coord)
                    {
                        Console.WriteLine($"here {coord[0]} {coord[1]}");
                        Console.WriteLine(visited[word[index]]);
                        Console.WriteLine(word[index]);
                        remove = i;
                        found = true;
                        break;
                    }
                    else
                    {

                    }
                }
                if (!found)
                {
                    visited[word[index]].Add(coord);
                    remove = visited[word[index]].Count;
                }

            }
            else
            {
                visited[word[index]] = [coord];
            }
            if (!found)
            {
                bool res = Dfs(board, word, coord[0], coord[1], index + 1);
                if (res)
                {
                    Console.WriteLine("returning here");
                    Console.WriteLine(index);
                    Console.WriteLine($"{y} {x}");
                    return true;
                }
                visited[word[index]].RemoveAt(remove);
            }
        }
        return false;
    }
}