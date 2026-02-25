public class Solution {
    public int[] SortByBits(int[] arr) {
        int n = arr.Length;
        Dictionary<int,int> dict = new();
        int num;
        int temp;
        int cnt;
        for(int i = 0; i<n; i++){
            num = arr[i];
            if(dict.ContainsKey(num)){
                continue;
            }
            cnt = 0;
            while(num > 0){
                temp = num;
                temp>>=1;
                temp<<=1;
                if(temp!=num){
                    cnt++;
                }
                num>>=1;
            }
            dict.Add(arr[i], cnt);
        }
        
        Array.Sort(arr, (a, b) => {
            int comparison = dict[a].CompareTo(dict[b]);
            if(comparison != 0)
                return comparison;
            return a.CompareTo(b);
        });
        return arr;
    }
}