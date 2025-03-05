public class Solution
{
    public long ColoredCells(int n)
    {
        long res = 1;
        n--;

        while (n > 0)
        {
            res += n * 4;
            n--;
        }
        return res;
    }
}
internal class Program
{
    static void Main(string[] args)
    {
        int n = 7;
        int output = 85;

        Solution obj = new();
        long res = obj.ColoredCells(n);
        Console.WriteLine(res);
        Console.WriteLine(output);
    }
}
