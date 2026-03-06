public class Solution {
    public bool CheckOnesSegment(string s) {
        int n = s.Length;
        bool foundone = false;
        bool foundzero = false;
        for(int i = 0; i<n; i++){
            if(s[i] == '1'){
                if(foundone == false){
                    foundone = true;
                }
                else if(foundzero == true){
                    return false;
                }
            }
            else if(foundone == true){
                foundzero = true;
            }
        }
        return true;
    }
}