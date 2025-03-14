public class Solution
{
    public int MaximumCandies(int[] candies, long k)
    {
        bool CanFeedKids(int pileSize, long unfedKids)
        {
            for (int i = 0; i < candies.Length; i++)
            {
                unfedKids -= candies[i] / pileSize;
                if (unfedKids <= 0)
                {
                    return true;
                }
            }
            return false;
        }
        int l = 1;
        int r = 0;
        long sum = 0;
        for (int i = 0; i < candies.Length; i++)
        {
            r = Math.Max(r, candies[i]);
            sum += candies[i];
        }
        if (sum < k)
        {
            return 0;
        }
        long tempk;
        int mid = 0;
        while (l <= r)
        {
            tempk = k;
            mid = l + ((r - l) / 2);
            if (CanFeedKids(mid, tempk))
            {
                l = mid + 1;
            }
            else
            {
                r = mid - 1;
            }
        }
        if (CanFeedKids(r + 1, k))
        {
            r++;
        }
        return r;
    }
}
internal class Program
{
    static void Main(string[] args)
    {
        int[] candies = [5, 8, 6];
        int k = 3;
        int output = 5;

        Solution obj = new();
        int res = obj.MaximumCandies(candies, k);
        Console.WriteLine(res);
        Console.WriteLine(output);
    }
}
