public class Solution
{
    public int[] ResultsArray(int[][] queries, int k)
    {
        PriorityQueue<int, int> pq = new();
        int[] res = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++)
        {
            int x = queries[i][0];
            int y = queries[i][1];
            int dist = Math.Abs(x) + Math.Abs(y);
            pq.Enqueue(dist, -dist);
            if (pq.Count > k)
                pq.Dequeue();
            int add = -1;
            if (pq.Count == k)
                add = pq.Peek();
            res[i] = add;
        }
        return res;
    }
}