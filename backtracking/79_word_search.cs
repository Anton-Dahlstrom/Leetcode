// Visited is not keeping preventing the same B from being used twice.
// Need to make sure gridsearch doesn't look at diagonal squares.


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
                    // return false;
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
        Console.WriteLine("grid");
        Console.WriteLine(target);
        IList<IList<int>> res = [];
        bool adding = true;
        for (int i = Math.Max(y - 1, 0); i < Math.Min(board.Length, y + 2); i++)
        {
            for (int j = Math.Max(x - 1, 0); j < Math.Min(x + 2, board[i].Length); j++)
            {
                Console.WriteLine($"HERE {i} {j}");
                if (i == y && j == x)
                {
                    continue;
                }
                if (board[i][j] == target)
                {
                    Console.WriteLine("FOUND");
                    if (visited.TryGetValue(target, out IList<IList<int>>? value))
                    {
                        foreach (IList<int> arr in value)
                        {
                            Console.WriteLine($"{arr[0]}, {arr[1]}  =?  {i} {j}");
                            if (arr[0] == i && arr[1] == j)
                            {
                                Console.WriteLine($"NOT RETURNING TO: {i} {j}");
                                adding = false;
                                break;
                            }
                        }
                        if (adding)
                        {
                            res.Add([i, j]);
                        }
                        adding = true;
                    }
                    else
                    {
                        res.Add([i, j]);
                    }
                }

            }
        }
        return res;
    }

    public bool Dfs(char[][] board, string word,
             int y, int x, int index)
    {
        IList<int> cur;
        Console.WriteLine("dfs");
        if (index >= word.Length)
        {
            return true;
        }
        Console.WriteLine($"{y}, {x}");
        IList<IList<int>> coords = GridSearch(board, word[index], y, x);
        Console.WriteLine(coords.Count);
        // return false;
        foreach (IList<int> coord in coords)
        {
            cur = [y, x];
            if (visited.TryGetValue(word[index], out IList<IList<int>>? value))
            {
                value.Add(cur);
            }
            else
            {
                visited[word[index]] = [cur];
            }

            bool res = Dfs(board, word, coord[0], coord[1], index + 1);
            if (res)
            {
                Console.WriteLine("returning here");
                Console.WriteLine(index);
                Console.WriteLine($"{y} {x}");
                return true;
            }
            for (int i = visited[word[index]].Count - 1; i >= 0; i--)
            {
                if (visited[word[index]][i] == cur)
                {
                    Console.WriteLine("REMOVED");
                    visited[word[index]].RemoveAt(i);
                }
            }
        }
        return false;
    }
}