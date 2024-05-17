// TO DO:
// Need to make it so the visited coordinates gets added to the correct char in the visited dict.

public class Solution
{
    public bool Exist(char[][] board, string word)
    {
        Dictionary<char, IList<IList<int>>> visited = [];
        Dfs(board, word, visited, 0, 0, 0);
        for (int i = 0; i < board.Length; i++)
        {
            for (int j = 0; j < board[i].Length; j++)
            {
                bool result = Dfs(board, word, visited, i, j, 0);
                if (result)
                {
                    return true;
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
            Dictionary<char, IList<IList<int>>> visited, int x, int y)
    {
        Console.WriteLine("grid");
        Console.WriteLine(target);
        IList<IList<int>> res = [];
        bool adding = true;
        for (int i = Math.Max(y - 1, 0); i < Math.Min(board.Length, y + 1); i++)
        {
            for (int j = Math.Max(x - 1, 0); j < Math.Min(x + 1, board[i].Length); j++)
            {
                if (board[i][j] == target)
                    Console.WriteLine("FOUND");
                {

                    if (visited.TryGetValue(target, out IList<IList<int>>? value))
                    {
                        foreach (IList<int> arr in value)
                        {
                            if (arr[0] == i && arr[1] == j)
                            {
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
        Console.WriteLine(res.Count);
        return res;
    }

    public bool Dfs(char[][] board, string word,
            Dictionary<char, IList<IList<int>>> visited, int y, int x, int index)
    {
        Console.WriteLine("dfs");
        if (index >= word.Length)
        {
            return true;
        }
        IList<IList<int>> coords = GridSearch(board, word[index], visited, y, x);
        foreach (IList<int> coord in coords)
        {
            if (visited.TryGetValue(word[index], out IList<IList<int>>? value))
            {
                value.Add([y, x]);
            }
            else
            {
                IList<int> test = [y, x];
                visited[word[index]] = [test];
            }

            bool res = Dfs(board, word, visited, coord[0], coord[1], index + 1);
            if (res)
            {
                return true;
            }
        }
        return false;
    }
}