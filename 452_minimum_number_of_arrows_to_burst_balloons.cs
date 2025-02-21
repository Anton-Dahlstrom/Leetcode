public class Solution
{
    public int FindMinArrowShots(int[][] points)
    {
        PriorityQueue<(int, int), (int, int)> priorityQueue = new PriorityQueue<(int, int), (int, int)>();
        for (int i = 0; i < points.Length; i++)
        {
            priorityQueue.Enqueue((i, 0), (points[i][0], 0));
            priorityQueue.Enqueue((i, 1), (points[i][1], 1));
        }

        HashSet<int> open = [];
        int res = 0;
        while (priorityQueue.Count > 0)
        {
            (int, int) cur = priorityQueue.Dequeue();
            if (cur.Item2 == 0)
            {
                open.Add(cur.Item1);
            }
            else
            {
                if (open.Contains(cur.Item1))
                {
                    res++;
                    open = [];
                }
            }
        }
        return res;
    }
}
internal class Program
{
    static void Main(string[] args)
    {
        Solution obj = new();
        int[][] points = [[10, 16], [2, 8], [1, 6], [7, 12]];
        int output = 2;
        int res = obj.FindMinArrowShots(points);
        Console.WriteLine(res);
        Console.WriteLine(output);
        Console.WriteLine(res == output);
    }
}
