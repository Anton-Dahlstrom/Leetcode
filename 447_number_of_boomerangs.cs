public class Solution {
    public int NumberOfBoomerangs(int[][] points) {
        int n = points.Length;
        int res = 0;
        for(int i = 0; i<n; i++){
            // dist, count
            Dictionary<double, int> distcnt = new();
            for(int j = 0; j<n; j++){
                if(i == j)
                    continue;
                double dist = calcDist(points[i], points[j]);
                distcnt.TryGetValue(dist, out var cnt);
                res += cnt*2;
                distcnt[dist] = cnt+1;
            }
        }
        return res;
    }
    public double calcDist(int[] p1, int[] p2){
        double dist = Math.Pow(p1[0] - p2[0],2) + Math.Pow(p1[1] - p2[1],2);
        return dist;
    }
}