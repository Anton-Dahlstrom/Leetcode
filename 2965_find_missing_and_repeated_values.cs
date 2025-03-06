public class Solution
{
    public int[] FindMissingAndRepeatedValues(int[][] grid)
    {
        int repeat = -1;
        int n = grid.Length;
        int val;
        int size = n * n;
        int total = (int)((size / 2.0) * (size + 1));

        HashSet<int> visited = [];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                val = grid[i][j];
                if (visited.Contains(val))
                {
                    repeat = val;
                    continue;
                }
                visited.Add(val);
                total -= val;
            }
        }
        return [repeat, total];
    }
}
internal class Program
{
    static void Main(string[] args)
    {
        int[][] grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]];
        int[] output = [9, 5];

        Solution obj = new();
        int[] res = obj.FindMissingAndRepeatedValues(grid);
        Console.WriteLine(string.Join(" ", res));
        Console.WriteLine(string.Join(" ", output));
    }
}
