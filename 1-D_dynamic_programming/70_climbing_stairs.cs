public class Solution
{
    public int ClimbStairs(int n)
    {
        int[] array = new int[n];
        array[0] = 1;
        if (n > 1) { array[1] = 2; }
        int i = 2;
        while (i < array.Length)
        {
            array[i] = array[i - 1] + array[i - 2];
            i++;
        }
        return array[^1];
    }
}