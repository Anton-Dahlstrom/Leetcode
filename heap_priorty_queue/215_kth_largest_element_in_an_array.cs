using System.Globalization;

public class MaxHeap
{
    public void Heapify(int[] array)
    {
        for (int i = array.Length - 1; i >= 0; i--)
        {
            MoveUp(array, i);
        }
    }
    public void MoveUp(int[] array, int child)
    {
        int parent = (child - 1) / 2;
        while (child > 0 && parent >= 0 && array[child] > array[parent])
        {
            (array[child], array[parent]) = (array[parent], array[child]);
            child = parent;
            parent = (child - 1) / 2;
        }
    }
    public void MoveDown(int[] array, int parent)
    {
        int len = array.Length;
        int child;
        int child1 = parent * 2 + 1;
        int child2 = parent * 2 + 2;
        while ((child2 < len && array[parent] < array[child2])
        || (child1 < len && array[parent] < array[child1]))
        {
            if (child2 < len)
            {
                if (array[child1] < array[child2])
                {
                    child = child1;
                }
                else { child = child2; }
            }
            else { child = child1; }
            (array[child], array[parent]) = (array[parent], array[child]);
            parent = child;
            child1 = parent * 2 + 1;
            child2 = parent * 2 + 2;
        }
    }
}

public class Solution
{
    public int FindKthLargest(int[] nums, int k)
    {
        MaxHeap heap = new MaxHeap();
        foreach (int val in nums)
        {
            Console.WriteLine(val);
        }
        heap.Heapify(nums);
        Console.WriteLine("--------------");
        foreach (int val in nums)
        {
            Console.WriteLine(val);
        }
        return 0;
    }
}