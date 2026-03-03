public class Solution {
    public char FindKthBit(int n, int k) {
        string cur = "0";
        for(int i = 1; i<n; i++){
            int size = cur.Length;
            char[] inverted = new char[size];
            for(int j = 0; j < size; j++){
                if(cur[j] == '0')
                    inverted[size-1-j] = '1';
                else
                    inverted[size-1-j] = '0';
            }
            string reversed = new string(inverted);
            cur = cur + "1" + reversed;
        }
        return cur[k-1];
    }
}