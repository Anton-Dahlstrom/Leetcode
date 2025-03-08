public class Solution
{
    public int[] ClosestPrimes(int left, int right)
    {
        if (left == right)
        {
            return [-1, -1];
        }
        if (left < 3)
        {
            return [2, 3];
        }

        int[] primes = new int[right + 1];
        int increment;
        int prevprime = 1;
        int diff = right + 1;
        int[] res = [-1, -1];
        for (int i = 2; i < primes.Length; i++)
        {
            if (primes[i] == 0)
            {
                increment = i;
                if (i > 2)
                {
                    increment *= 2;
                }
                for (int j = i + increment; j <= right; j += increment)
                {
                    primes[j] = 1;
                }
                if (prevprime >= left && i - prevprime < diff)
                {
                    diff = i - prevprime;
                    if (prevprime >= left)
                    {
                        res[0] = prevprime;
                        res[1] = i;
                    }
                }
                prevprime = i;
            }
        }
        return res;
    }
}

internal class Program
{
    static void Main(string[] args)
    {
        int left = 19;
        int right = 31;
        int[] output = [29, 31];

        Solution obj = new();
        int[] res = obj.ClosestPrimes(left, right);
        Console.WriteLine(string.Join(" ", res));
        Console.WriteLine(string.Join(" ", output));
        Console.WriteLine(res == output);
    }
}
