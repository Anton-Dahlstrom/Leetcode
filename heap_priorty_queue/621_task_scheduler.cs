public class Solution
{
    public int LeastInterval(char[] tasks, int n)
    {
        Dictionary<char, int> hmap = new Dictionary<char, int>();
        foreach (char key in tasks)
        {
            if (hmap.ContainsKey(key))
            {
                hmap[key]++;
            }
            else
            {
                hmap.Add(key, 1);
            }
        }
        return 0;
    }
}