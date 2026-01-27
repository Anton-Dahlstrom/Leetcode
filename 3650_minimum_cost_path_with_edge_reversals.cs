public class Solution
{
    public int MinCost(int n, int[][] edges)
    {
        // from, <to, weight>
        Dictionary<int, List<(int Node, int Weight)>> graph = new();
        foreach (var edge in edges)
        {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            if (!graph.ContainsKey(u))
                graph[u] = new List<(int Node, int Weight)>();
            graph[u].Add((v, w));
            if (!graph.ContainsKey(v))
                graph[v] = new List<(int Node, int Weight)>();
            graph[v].Add((u, w * 2));
        }

        // node, curcost
        PriorityQueue<int, int> pq = new();
        pq.Enqueue(0, 0);
        // node, best
        Dictionary<int, int> visited = new();
        int res = int.MaxValue;

        while (pq.TryDequeue(out int node, out int cost))
        {
            if (cost >= res)
                return res;
            if (graph.TryGetValue(node, out var list))
            {
                foreach (var e in list)
                {
                    int total = e.Weight + cost;
                    if (visited.TryGetValue(e.Node, out int best))
                    {
                        if (total >= best)
                            continue;
                    }
                    visited[e.Node] = total;
                    pq.Enqueue(e.Node, total);
                    if (e.Node == n - 1)
                    {
                        res = Math.Min(res, total);
                    }
                }
            }
        }
        return -1;
    }
}