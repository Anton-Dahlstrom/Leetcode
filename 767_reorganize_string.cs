public class Solution
{
    public string ReorganizeString(string s)
    {
        Dictionary<char, int> hmap = new();
        foreach (char chr in s)
        {
            hmap.TryGetValue(chr, out int cnt);
            hmap[chr] = cnt + 1;
        }
        PriorityQueue<char, int> pq = new();
        foreach (var key in hmap)
        {
            pq.Enqueue(key.Key, -key.Value);
        }
        string res = "";
        while (pq.TryDequeue(out char chr, out int cnt))
        {
            if (res.Length > 0 && chr == res[^1])
            {
                if (pq.TryDequeue(out char chr2, out int cnt2))
                {
                    res += chr2;
                    cnt2++;
                    if (cnt2 < 0)
                        pq.Enqueue(chr2, cnt2);
                }
                else
                {
                    return "";
                }
            }
            res += chr;
            cnt++;
            if (cnt < 0)
                pq.Enqueue(chr, cnt);
        }
        return res;
    }
}