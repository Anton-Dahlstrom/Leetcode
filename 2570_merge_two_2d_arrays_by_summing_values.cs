public class Solution
{
    public int[][] MergeArrays(int[][] nums1, int[][] nums2)
    {
        List<int[]> res = [];
        int i = 0;
        int j = 0;

        while (i < nums1.Length || j < nums2.Length)
        {

            if (i < nums1.Length && j < nums2.Length)
            {
                if (nums1[i][0] == nums2[j][0])
                {
                    res.Add([nums1[i][0], nums1[i][1] + nums2[j][1]]);
                    i++;
                    j++;
                }
                else if (nums1[i][0] < nums2[j][0])
                {
                    res.Add([nums1[i][0], nums1[i][1]]);
                    i++;
                }
                else
                {
                    res.Add([nums2[j][0], nums2[j][1]]);
                    j++;
                }
                continue;


            }
            if (i < nums1.Length)
            {
                res.Add([nums1[i][0], nums1[i][1]]);
                i++;
            }
            else
            {
                res.Add([nums2[j][0], nums2[j][1]]);
                j++;
            }
        }
        return [.. res];
    }
}

internal class Program
{
    static void Main(string[] args)

    {
        int[][] nums1 = [[1, 2], [2, 3], [4, 5]];
        int[][] nums2 = [[1, 4], [3, 2], [4, 1]];
        int[][] output = [[1, 6], [2, 3], [3, 2], [4, 6]];
        Solution obj = new();
        int[][] res = obj.MergeArrays(nums1, nums2);
        Console.WriteLine("[" + string.Join(",", output.Select(row => "[" + string.Join(",", row) + "]")) + "]");
        Console.WriteLine("[" + string.Join(",", res.Select(row => "[" + string.Join(",", row) + "]")) + "]");
        Console.WriteLine(res == output);
    }
}
