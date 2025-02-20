public class Solution
{
    public int LeastInterval(char[] tasks, int n)
    {
        Dictionary<char, int> hmap = [];
        int m = tasks.Length;
        int max = 0;
        int maxcount = 0;

        for (int i = 0; i < m; i++)
        {
            hmap[tasks[i]] = hmap.GetValueOrDefault(tasks[i], 0) + 1;
            if (hmap[tasks[i]] == max)
            {
                maxcount += 1;
            }
            else if (hmap[tasks[i]] > max)
            {
                max = hmap[tasks[i]];
                maxcount = 0;
            }


        }
        return Math.Max((max + (max - 1) * n) + maxcount, m);
    }
}
