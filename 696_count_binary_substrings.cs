public class Solution {
    public int CountBinarySubstrings(string s) {
        int res = 0;
        int prev = 0;
        int cur = 0;
        for(int i = 0; i<s.Length; i++){
            if(i>0 && s[i]!= s[i-1]){
                prev = cur;
                cur = 0;
            }
            cur++;
            if(cur <= prev){
                res ++;
            }
        }
        return res;
    }
}