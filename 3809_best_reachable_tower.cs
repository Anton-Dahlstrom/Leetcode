public class Solution
{
    public int[] BestTower(int[][] towers, int[] center, int radius)
    {
        // x,y,quality
        // reachable if man dist <= radius
        // center is my location
        int n = towers.Length;
        var res = new int[2] { -1, -1 };
        int bestquality = -1;
        for (int i = 0; i < n; i++)
        {
            int dist = 0;
            dist += Math.Abs(center[0] - towers[i][0]) + Math.Abs(center[1] - towers[i][1]);
            // reachable
            if (dist <= radius)
            {
                if (bestquality < towers[i][2] || (bestquality == towers[i][2] && (towers[i][0] < res[0] || (towers[i][0] == res[0] && towers[i][1] < res[1]))))
                {
                    res[0] = towers[i][0];
                    res[1] = towers[i][1];
                    bestquality = towers[i][2];
                }
            }
        }
        return res;
    }
}