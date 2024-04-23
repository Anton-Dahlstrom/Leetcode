public class MaxHeap
{
    public void Heapify(int[] array)
    {

    }
    public void MoveDown(int[] array, int parent)
    {
        int len = array.Length;
        int child1 = parent * 2 + 1;
        int child2 = parent * 2 + 2;
        if ((child2 <= len && array[parent] < array[child2])
        || (child1 <= len && array[parent] < array[child1]))
        {

        }
    }
}

public class Solution
{
    public int FindKthLargest(int[] nums, int k)
    {
        int[] stack = [];
        int length = nums.Length;
        Console.WriteLine(length);
        foreach (int num in nums)
        {
            Console.WriteLine(num);
        }
        return 0;
    }
}