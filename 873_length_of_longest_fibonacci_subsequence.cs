public class Solution
{
    public int LenLongestFibSubseq(int[] arr)
    {
        HashSet<int> set = [.. arr];
        int res = 0;
        int temp = 0;
        int n1 = 0;
        int n2 = 0;
        for (int i = 0; i < arr.Length; i++)
        {
            for (int j = i + 1; j < arr.Length; j++)
            {
                n1 = arr[i];
                n2 = arr[j];
                temp = 0;
                while (set.Contains(n1 + n2))
                {
                    temp++;
                    (n1, n2) = (n2, n1 + n2);
                }
                res = Math.Max(res, temp);
            }

        }
        if (res > 0)
        {
            res += 2;
        }
        return res;
    }
}

internal class Program
{
    static void Main(string[] args)

    {
        // 4, 14, 18, 32, 50, 
        int[] arr = arr = [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50];
        int output = 5;

        Solution obj = new();
        int res = obj.LenLongestFibSubseq(arr);
        Console.WriteLine(res);
        Console.WriteLine(output);
        Console.WriteLine(res == output);
    }
}
public class Solution
{
    public int LenLongestFibSubseq(int[] arr)
    {
        HashSet<int> set = [.. arr];
        int res = 0;
        int temp = 0;
        int n1 = 0;
        int n2 = 0;
        for (int i = 0; i < arr.Length; i++)
        {
            for (int j = i + 1; j < arr.Length; j++)
            {
                n1 = arr[i];
                n2 = arr[j];
                temp = 0;
                while (set.Contains(n1 + n2))
                {
                    temp++;
                    (n1, n2) = (n2, n1 + n2);
                }
                res = Math.Max(res, temp);
            }

        }
        if (res > 0)
        {
            res += 2;
        }
        return res;
    }
}

internal class Program
{
    static void Main(string[] args)

    {
        // 4, 14, 18, 32, 50, 
        int[] arr = arr = [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50];
        int output = 5;

        Solution obj = new();
        int res = obj.LenLongestFibSubseq(arr);
        Console.WriteLine(res);
        Console.WriteLine(output);
        Console.WriteLine(res == output);
    }
}
