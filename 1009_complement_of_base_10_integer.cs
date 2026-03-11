public class Solution {
    public int BitwiseComplement(int n) {
        if(n==0)
            return 1;
        int i = 1;
        while(i<=n){
            i<<=1;
        }
        i-=1;
        return n ^ i;
    }
}