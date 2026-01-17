public class Solution
{
    public int MaximizeSquareArea(int m, int n, int[] hFences, int[] vFences)
    {
        // hfence = n
        Array.Sort(hFences);
        Array.Sort(vFences);
        List<int> hFenceslist = hFences.ToList();
        hFenceslist.Add(m);
        List<int> vFenceslist = vFences.ToList();
        vFenceslist.Add(n);

        int MOD = (int)Math.Pow(10, 9) + 7;
        HashSet<int> hset = new();
        List<int> gaplist = new();
        int prev = 1;
        // can use hset earlier, there is no reason to make 2+3 twice
        for (int i = 0; i < hFenceslist.Count; i++)
        {
            List<int> temp = new();
            int gap = hFenceslist[i] - prev;
            hset.Add(gap);
            temp.Add(gap);
            foreach (int hgap in gaplist)
            {
                hset.Add(hgap + gap);
                temp.Add(hgap + gap);
            }
            prev = hFenceslist[i];
            gaplist = temp;
        }

        int res = -1;
        prev = 1;
        gaplist = new();
        for (int i = 0; i < vFenceslist.Count; i++)
        {
            List<int> temp = new();
            int gap = vFenceslist[i] - prev;
            temp.Add(gap);
            if (hset.Contains(gap))
            {
                res = Math.Max(res, gap);
            }
            foreach (int vgap in gaplist)
            {
                int combined = vgap + gap;
                if (hset.Contains(combined))
                {
                    res = Math.Max(res, combined);
                }
                temp.Add(combined);
            }
            prev = vFenceslist[i];
            gaplist = temp;
        }
        if (res < 0)
        {
            return res;
        }
        return (int)((long)res * res % MOD);
    }
}