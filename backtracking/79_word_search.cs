public class Solution
{
    public IList<IList<int>> Exist(string[][] board, string word)
    {
        Dfs([.. nums], 0, 0, target);
        foreach (IList<int> l in result)
        {
            foreach (int num in l)
            {
                Console.Write(num);
            }
            Console.WriteLine("");
            Console.WriteLine("--");
        }
        return result;
    }

    // Need to make sure the GridSearch function doesn't try to visit a previous node.
    // Maybe by having a hashmap with each previously written letter as the key and a list
    // of coordinates as values, when a match is found it checks if the coordinates are
    // identical to any of the coordinate values in the hashmap and if so skips that coordinate.
    public IList<IList<int>> GridSearch(char[][] board, int x, int y, int index, string target)
    {
        IList<IList<int>> res = [];
        for (int i = Math.Max(y - 1, 0); i < Math.Min(board.Length, y + 1); i++)
        {
            for (int j = Math.Max(x - 1, 0); j < Math.Min(x + 1, board[i].Length); j++)
            {
                if (board[i][j] == target[index])
                {
                    res.Add([i, j]);
                }

            }
        }
        return res;
    }
}