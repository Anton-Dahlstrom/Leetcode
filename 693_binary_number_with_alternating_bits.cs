public class Solution {
    public bool HasAlternatingBits(int n) {
        var binary = Convert.ToString(n, 2);
        for(int i = 1; i < binary.Length; i++){
            if(binary[i] == binary[i-1])
                return false;
        }
        return true;
    }
}