public class Solution {
    public int MinOperations(string s) {
        int n = s.Length;
        int evenstart = 0;
        int oddstart = 0; 
        for(int i = 0; i<n; i++){
            if((i%2) + s[i] - '0' == 1){
                evenstart++;
            }
            else{
                oddstart++;
            }
        }
        return Math.Min(evenstart, oddstart);
    }
}