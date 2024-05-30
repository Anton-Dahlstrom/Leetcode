public class Solution
{
    public int[] Mergesort(int[] array)
    {
        int len = array.Length;
        int mid = array.Length / 2;
        int[] left = new int[mid];
        int[] right = new int[array.Length - mid];
        Array.Copy(array, 0, left, 0, mid);
        Array.Copy(array, mid, right, 0, mid);
        if (len > 2)
        {
            left = Mergesort(left);
            right = Mergesort(right);

        }
        else if (len <= 1)
        {
            return array;
        }
        int l = 0;
        int r = 0;
        int p = 0;
        while (l < left.Length && r < right.Length)
        {
            if (left[l] < right[r])
            {
                array[p] = left[l];
                l++;
            }
            else
            {
                array[p] = right[r];
                r++;
            }
            p++;
        }
        while (l < left.Length)
        {
            array[p] = left[l];
            l++;
            p++;
        }
        while (r < right.Length)
        {
            array[p] = right[r];
            r++;
            p++;
        }
        return array;
    }
    public int Ciel(int num, int den)
    {
        return (num + (den - 1)) / den;
    }
    // The value of the smaller elements divided by x will always be smaller than the largest element divided by x.
    // This means that if h >= piles.Length * 3 then the largest value in piles divided by 3 is our maximum possible
    // value for x because it's guaranteed to also "fit" into the smaller values atleast 3 times.
    public int MinEatingSpeed(int[] piles, int h)
    {
        piles = Mergesort(piles);
        int div = h / piles.Length;
        int spare = h % piles.Length;
        // The solution has to be somewhere between the values of min and max.
        // The value of spare will increase as we find and values in the array that don't need
        // to use all eating sessions of div to be fully eaten.
        // When spare becomes larger than the length of piles we can increase div and check again
        // if we can find more spares.
        int min = Ciel(piles[0], div);
        int max = Ciel(piles[^1], div);
        if (min == max)
        {
            return min;
        }
        Console.WriteLine(min);
        Console.WriteLine(max);
        Console.WriteLine(spare);
        return 0;
    }
}