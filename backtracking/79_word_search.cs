public class Solution
{
    Dictionary<(int, int), int> visited = [];
    public bool Exist(char[][] board, string word)
    {
        for (int i = 0; i < board.Length; i++)
        {
            for (int j = 0; j < board[i].Length; j++)
            {
                if (board[i][j] == word[0])
                {
                    visited[(i, j)] = 1;
                    bool result = Dfs(board, word, i, j, 1);
                    visited.Remove((i, j));
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

    public bool Dfs(char[][] board, string word,
             int y, int x, int index)
    {
        bool res = false;
        if (index >= word.Length)
        {
            return true;
        }
        for (int j = x - 1; j < Math.Min(x + 2, board[0].Length); j += 2)
        {
            if (j < 0)
            {
                continue;
            }
            else if (board[y][j] == word[index])
            {

                if (!visited.TryGetValue((y, j), out int visitedY))
                {
                    visited[(y, j)] = 1;
                    res = Dfs(board, word, y, j, index + 1);
                    visited.Remove((y, j));
                    if (res)
                    {
                        return true;
                    }
                }
            }
        }
        for (int i = y - 1; i < Math.Min(board.Length, y + 2); i += 2)
        {
            if (i < 0)
            {
                continue;
            }
            else if (board[i][x] == word[index])
            {
                if (!visited.TryGetValue((i, x), out int visitedY))
                {
                    visited[(i, x)] = 1;
                    res = Dfs(board, word, i, x, index + 1);
                    visited.Remove((i, x));
                    if (res)
                    {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}