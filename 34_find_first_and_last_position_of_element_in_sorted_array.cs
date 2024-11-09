public class Solution
{
    public int[] SearchRange(int[] nums, int target)
    {
        int[] res = [-1, -1];
        int BinarySearch(int[] nums, int target)
        {
            int l = 0;
            int r = nums.Length - 1;
            int mid;
            while (l <= r)
            {
                mid = l + ((r - l) / 2);
                Console.WriteLine($"{l} {r} {mid}");
                if (nums[mid] == target) { return mid; }
                else if (nums[mid] < target) { l = mid + 1; }
                else { r = mid - 1; }
            }
            return -1;
        }
        int found = BinarySearch(nums, target);
        if (found < 0) { return res; }
        int i = found;
        int l = 0;
        int mid;
        while (true)
        {
            if (nums[l] == target)
            {
                res[0] = l;
                break;
            }
            if (nums[i] != target)
            {
                res[0] = i + 1;
                break;
            }
            mid = l + ((i - l) / 2);
            if (nums[mid] != target) { l = mid + 1; }
            else { i = mid - 1; }
        }
        i = found;
        int r = nums.Length - 1;
        while (true)
        {
            Console.WriteLine($"{i} {r}");
            if (nums[r] == target)
            {
                res[1] = r;
                break;
            }
            if (nums[i] != target)
            {
                res[1] = i - 1;
                break;
            }
            mid = i + ((r - i) / 2);
            if (nums[mid] != target) { r = mid - 1; }
            else { i = mid + 1; }
        }

        return res;
    }
}