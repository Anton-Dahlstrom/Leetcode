public class Solution {
    public bool CanPlaceFlowers(int[] flowerbed, int n) {
        if(n==0)
            return true;
        int m = flowerbed.Length;
        int count = 0;
        for(int i = 0; i<m; i++){
            int flowers = 0;
            if((i > 0 && flowerbed[i-1] == 1) || flowerbed[i] == 1 || (i<m-1 && flowerbed[i+1] == 1)){
                continue;
            }
            count++;
            i++;
            if(count == n)
                return true;
        }
        return false;
    }
}