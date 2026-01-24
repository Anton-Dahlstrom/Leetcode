public class Solution {
    public IList<IList<int>> KSmallestPairs(int[] nums1, int[] nums2, int k) {
        int n = nums1.Length;
        int m = nums2.Length;
        PriorityQueue<(int index1, int index2), int> pq = new();
        for(int i = 0; i<n; i++){
            pq.Enqueue((i, 0),nums1[i]+nums2[0]);
        }
        IList<IList<int>> res = new List<IList<int>>();
        while(k>0){
            var cur = pq.Dequeue();
            res.Add([nums1[cur.index1],nums2[cur.index2]]);
            if(cur.index2<m-1){
                pq.Enqueue((cur.index1, cur.index2+1), nums1[cur.index1]+ nums2[cur.index2+1]);
            }
            k--;
        }
        return res;
    }
}